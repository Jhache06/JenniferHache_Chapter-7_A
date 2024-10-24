# Import regular expression module
import re

# Create empty list to store sentences
paragraphs = []

# Use while loop to ask user to enter their sentences. Ask user to enter 'done' when finished.
while True:
    paragraph = input("Enter your sentences here, type 'done' when finished: ")
    if paragraph.lower() == 'done':
        break
    # Append the entered paragraph to the empty list
    paragraphs.append(paragraph)

# Use the .join method to incorporate all sentences as one string
all_sentences = ' '.join(paragraphs)

# Split the combined string into individual sentences using regex
pat_sentences = re.split(r'[A-Z].*?[.!?](?= [A-Z]|$)', all_sentences)

# Count the sentences
count_sentences = len(paragraphs)

# print the total amount of sentences entered by user
print(f'Your sentence count is: {count_sentences}')
