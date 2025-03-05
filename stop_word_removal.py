"""
Stopword Removal 🚫 Challenge: 
Develop a function that removes stopwords 
(commonly used words) from a given sentence or text. 
"""

def stop_word_removal(text):
    # expand as needed
    stop_words = {
        'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 
        'has', 'he', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 
        'to', 'was', 'were', 'will', 'with', 'i', 'you', 'your', 'am'
    }

    text = text.lower().split()
    text = [word for word in text if word not in stop_words]
    text = ' '.join(text)

    return text

text = 'I am a computer scientist who practices coding.'
print(stop_word_removal(text=text))


