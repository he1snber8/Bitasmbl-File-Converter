# simple content-type validation
ALLOWED = {"application/pdf","image/png","image/jpeg"}

def is_allowed(content_type: str) -> bool:
    return content_type in ALLOWED
