import re
from .utils import log_and_profile

@log_and_profile
def validate_contract(text):
    required_clauses = ["Term", "Payment", "Confidentiality", "Termination"]
    missing_clauses = [clause for clause in required_clauses if clause.lower() not in text.lower()]

    dates = re.findall(r'\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b', text)

    amounts = re.findall(r'\$\d+(?:,\d{3})*(?:\.\d{2})?', text)

    return {
        "missing_clauses": missing_clauses,
        "dates": dates,
        "amounts": amounts
    }
