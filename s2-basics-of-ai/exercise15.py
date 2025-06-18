import re

def clean_text(text):
  print(text)
  # remove punctuation
  # match any character that is not word (\w) or whitespace (\s) character
  text = re.sub(r"[^\w\s]", "", text)
  text = text.strip()
  text = text.split()
  # remove extra spaces
  text = " ".join(text)
  # covert to lowercase
  return text.lower()

input_text = "   Hello, World.!!! Welcome to Python, Programming...      "
cleaned_text = clean_text(input_text)
print("Cleaned Text: ", cleaned_text)
