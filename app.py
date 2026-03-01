from preprocessing.preprocess import clean_text
from nlp_module.extractor import extract_classes
from uml_generator.plantuml_generator import generate_plantuml

# Read SRS file
with open("input/sample_srs.txt", "r") as f:
    text = f.read()

# Step 1: Preprocess text
cleaned_text = clean_text(text)

# Step 2: Extract UML Classes using NLP
classes = extract_classes(cleaned_text)

print("Detected Classes:", classes)

# Step 3: Generate UML Diagram
generate_plantuml(classes)

print("PlantUML File Generated Successfully!")
