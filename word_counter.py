"""
Word Frequency Counter 📊 Challenge: 
Write a Python function that takes a text document 
as input and returns a dictionary containing the 
frequency of each word in the document.
"""

def word_freq_counter(text):
    counter_dict = {}
    punctuations = '''!@#$%^&*()/?;,.()[]'''
    for char in punctuations:
        text = text.replace(char, '')
    
    for word in text.split():
        if word:
            if word not in counter_dict:
                counter_dict[word] = 1
            else:
                counter_dict[word] += 1
    
    return counter_dict

sample_input= "Aria is practicing nlp. Aria is looking for a job."
print(word_freq_counter(sample_input))