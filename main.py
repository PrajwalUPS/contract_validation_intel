# main.py

from contract_validation.text_extraction import extract_text_from_pdf
from contract_validation.summarization import summarize_text
from contract_validation.validation import validate_contract
from contract_validation.ner import extract_entities
from contract_validation.classification import classify_text
from contract_validation.comparison import compare_texts
from contract_validation.highlighting import highlight_differences

def process_contract(pdf_path, template_text, output_highlight_path):
    text = extract_text_from_pdf(pdf_path)
    summary = summarize_text(text)
    validation_results = validate_contract(text)
    entities = extract_entities(text)
    classification = classify_text(text)
    similarity = compare_texts(text, template_text)

    highlight_differences(pdf_path, template_text, output_highlight_path)

    return {
        "text": text,
        "summary": summary,
        "validation_results": validation_results,
        "entities": entities,
        "classification": classification,
        "similarity": similarity
    }

# Example usage
if __name__ == "__main__":
    pdf_path = 'path/to/your/contract.pdf'
    template_text = 'Standard contract template text...'
    output_highlight_path = 'path/to/output/contract_highlighted.pdf'
    results = process_contract(pdf_path, template_text, output_highlight_path)
    print("Extracted Text:", results['text'])
    print("Summary:", results['summary'])
    print("Validation Results:", results['validation_results'])
    print("Entities:", results['entities'])
    print("Classification:", results['classification'])
    print("Similarity:", results['similarity'])
