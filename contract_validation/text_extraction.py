import PyPDF2
from pdf2image import convert_from_path
from PIL import Image
from openvino.runtime import Core
import numpy as np
from .utils import log_and_profile

# Initialize OpenVINO OCR
ie_core = Core()
ocr_model = ie_core.read_model(model='models/ocr_model.xml')
compiled_model = ie_core.compile_model(model=ocr_model, device_name='CPU')
ocr_input_layer = compiled_model.input(0)
ocr_output_layer = compiled_model.output(0)

@log_and_profile
def extract_text_from_pdf(pdf_path):
    text = ""

    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfFileReader(file)
            for page_num in range(reader.numPages):
                text += reader.getPage(page_num).extract_text()
    except Exception as e:
        print(f"Failed to extract text using PyPDF2: {e}")

    if not text or len(text.split()) < 50:
        text = ""
        images = convert_from_path(pdf_path)
        for img in images:
            img = img.convert('RGB')
            img = np.array(img)
            input_blob = {ocr_input_layer: img}
            result = compiled_model.infer_new_request(input_blob)
            text += result[ocr_output_layer]

    return text
