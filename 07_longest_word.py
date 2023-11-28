'''

Problem: Find the Longest Word in a Sentence

Write a Python function that takes a sentence as input and returns the longest word in that sentence. 
In case of a tie, return the first word that reaches the maximum length.


'''



def find_longest_word(sentence):
    words = sentence.split()

    longest_word = words[0]

    for word in words:
        # If the current word is longer than the longest word found so far, update the longest word
        if len(word) > len(longest_word):
            longest_word = word

    return longest_word

test_sentences = [
    "This is an example sentence",
    "Short sentences work too"
]

longest_words = {}

for sentence in test_sentences:
    longest_word_in_sentence = find_longest_word(sentence)
    longest_words[sentence] = longest_word_in_sentence

print(longest_words)