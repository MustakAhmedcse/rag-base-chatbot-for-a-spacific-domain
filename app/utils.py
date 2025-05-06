import re
import logging

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def is_bangla(text: str) -> bool:
    bangla_pattern = re.compile(r'[\u0980-\u09FF]')
    result = bool(bangla_pattern.search(text))
    logging.info(f"is_bangla('{text[:30]}...'): {result}")
    return result

def is_relevant_to_retailer_app(question: str) -> bool:
    retailer_keywords = [
        "retailer", "banglalink", "app", "profile", "device", "registration",
        "feedback", "voice of retailer", "commission", "lifting", "dashboard",
        "login", "logout", "edit", "submit", "form", "operator", "category"
    ]
    question_lower = question.lower()
    result = any(keyword in question_lower for keyword in retailer_keywords)
    logging.info(f"is_relevant_to_retailer_app('{question[:30]}...'): {result}")
    return result
