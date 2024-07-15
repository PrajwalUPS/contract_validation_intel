import fitz
from nltk.tokenize import word_tokenize
from .utils import log_and_profile

@log_and_profile
def highlight_differences(pdf_path, template_text, output_path):
    doc = fitz.open(pdf_path)
    template_words = set(word_tokenize(template_text.lower()))

    for page_num in range(len(doc)):
        page = doc[page_num]
        words = page.get_text("words")
        for word in words:
            word_text = word[4].lower()
            if word_text not in template_words:
                highlight = page.add_highlight_annot(fitz.Rect(word[:4]))
                highlight.update()

    doc.save(output_path, garbage=4, deflate=True, clean=True)
