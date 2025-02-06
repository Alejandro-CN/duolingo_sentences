import unicodedata
import string
from datetime import datetime


# Function to remove space after an apostrophe and trailing punctuation
def apostro_space(sentence):
  new_sentence = ""
  i = 0
  while i < len(sentence):
    char = sentence[i]
    if char == "'" and i + 1 < len(sentence) and sentence[i + 1] == " ":
      new_sentence += "'"
      i += 2  # Skip the space
    else:
      new_sentence += char
      i += 1
  # Remove the period if it exists at the end of the sentence
  if new_sentence[-1:] in ['.', '!', '?']:
      new_sentence = new_sentence[:-1]
  return new_sentence.strip()

# Remove accents, punctuation, and convert to lowercase
def clean_text(text):
    #Run the "apostro_space" function
    text = apostro_space(text)
    # Normalize the text to decompose accented characters into their base characters and combining diacritics
    normalized_text = unicodedata.normalize('NFD', text)
    # Build a new string, excluding combining characters (category 'Mn') and punctuation
    no_accents_text = ''.join(
        char for char in normalized_text
        if unicodedata.category(char) != 'Mn' and (char not in string.punctuation or char == "'")
    )
    # Replace the 'œ' character with 'oe'
    no_accents_text = no_accents_text.replace('œ', 'oe').replace('Œ', 'Oe')
    # Return the string with all accents and punctuation removed, strip any leading/trailing spaces, and convert to lower case
    return no_accents_text.strip().lower()

# Get a timestamp
def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
