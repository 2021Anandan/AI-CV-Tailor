import re


def tokenize(text: str) -> set[str]:
    """
    Convert text into a normalized set of keywords.
    """

    words = re.findall(r"[a-zA-Z0-9+#.]+", text.lower())

    return set(words)
