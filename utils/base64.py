import base64

def convertion_to_base64(text: str) -> str:
    """Convert text to base64"""
    return base64.b64encode(text.encode()).decode()