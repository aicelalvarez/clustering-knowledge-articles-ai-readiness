import re

def strip_html(text: str) -> str:
    """
    Simple HTML stripping used in notebook to support tokenization.
    Keeps text content only.
    """
    return re.sub(r"<[^>]+>", " ", str(text))

def normalize_ws(text: str) -> str:
    """
    Normalize whitespace: collapse multiple spaces/newlines.
    """
    return re.sub(r"\s+", " ", str(text)).strip()
