import spacy
from .utils import log_and_profile

# Initialize spaCy NLP
nlp = spacy.load('en_core_web_sm')

@log_and_profile
def classify_text(text):
    doc = nlp(text)
    if doc.cats.get('CONTRACT', 0.0) > 0.5:
        return 'contract'
    else:
        return 'non-contract'
