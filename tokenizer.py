"""
Text Cleaning and Tokenization Challenge: 
Create a function to clean and tokenize a given text, 
removing punctuation and converting words to lowercase.
"""

def tokenize(text):
    punctuations = '''~!@#$%^&*,.()[]\{\}'''
    for char in text:
        if char in punctuations:
            text = text.replace(char,'')
    text = text.lower()
    text = text.split()
    return text

text = 'I am writing the code.'
print(tokenize(text=text))