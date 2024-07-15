import spacy
from .utils import log_and_profile

# Initialize spaCy NLP
nlp = spacy.load('en_core_web_sm')

@log_and_profile
def extract_entities(text):
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities
