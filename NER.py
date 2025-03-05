"""
Named Entity Recognition (NER) 🧐 Challenge: 
Implement a Named Entity Recognition algorithm 
that identifies and classifies named entities 
like names, locations, and organizations in a text. 
"""
from spacy import nlp

def my_ner(text):
    doc = nlp(text)
    entities = [(entity.text , entity.label_) for entity in doc.entities]

    return entities

text = 'I have worked at Ford and IEEE from home in Pennsylvania.'
print(my_ner(text=text))