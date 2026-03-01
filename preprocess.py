import re

# Function to clean and normalize text
def clean_text(text):
    # convert text to lowercase
    text = text.lower()

    # remove special characters
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)

    return text
  
