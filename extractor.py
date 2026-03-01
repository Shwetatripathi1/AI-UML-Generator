
import spacy

# Load English NLP model
nlp = spacy.load("en_core_web_sm")

# Function to extract possible UML classes
def extract_classes(text):
    doc = nlp(text)

    classes = set()

    # Identify nouns and proper nouns as classes
    for token in doc:
        if token.pos_ == "NOUN" or token.pos_ == "PROPN":
            classes.add(token.text.capitalize())

    return list(classes)
