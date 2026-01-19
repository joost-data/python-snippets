import string

def clean_text(text):
    """
    Lowercase text and remove punctuation.
    """
    text = text.lower()
    return text.translate(str.maketrans("", "", string.punctuation))

