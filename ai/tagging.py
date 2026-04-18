import spacy

# Load model ONCE
nlp = spacy.load("en_core_web_sm")


def generate_tags(text):
    doc = nlp(text)

    tags = []
    for token in doc:
        if token.pos_ in ["NOUN", "PROPN"]:
            tags.append(token.text)

    return list(set(tags))