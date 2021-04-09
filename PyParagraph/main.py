# Import modules
import os
import csv
import re
# Create path to .txt datafile
filepath = os.path.join("Resources", "paragraph_3.txt")
# Define lists
sentence_words = []
sentences_characters = []
# Open text file
with open(filepath) as txtfile:
    # read in passage as a "." delimited file - i.e. sentences
    sentence_reader = csv.reader(txtfile, delimiter =".")
    for sentences in sentence_reader:
        # remove the last entry in the list as its blank
        sentences.pop()
        # sentences is a python list where each 
        # entry is a sentence in the passage
    for x in range(len(sentences)):
            # Count the number of words per sentence and add to new list
            sentence_words.append(len(re.split(" ",sentences[x])))
            # Count the number of characters per sentence and add to new list
            sentences_characters.append(len(sentences[x]))

print()
print()
print("Paragraph Analysis  " + str(filepath))
print("---------------------------------------------")
print("Approximate Word Count: " + str(sum(sentence_words)))
print("Approximate Sentence Count: " + str(len(sentences)))
print("Average Letter Count: " + str(round(sum(sentences_characters)/sum(sentence_words),1)))
print("Average Sentence Length: " + str(round(sum(sentence_words)/len(sentences),1)))
