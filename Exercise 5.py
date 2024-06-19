"""
Exercise 5.
Write a function named uses_all that takes a word and a string of required letters,
and that returns True if the word uses all the required letters at least once.
How many words are there that use all the vowels aeiou? How about aeiouy?
"""

def uses_all ( word, required_letters):
    # Check if a word contains all the required letters at least once. Return True if all characters in required_letters are in the word, False otherwise.
    for letter in required_letters:
        if letter not in word:
            return False        
    return True

# How many words are there that use all the vowels aeiou? How about aeiouy?

def count_words_with_required_letters(filename, required_letters):
    # Count words from a file that use all the required letters at least once.
    words_with_required_letters = []

    # Open the file in read mode and iterate over each line (word)
    with open(filename, 'r') as fin:
        for line in fin:
            word = line.strip()  # Remove leading and trailing spaces
            if uses_all(word, required_letters):
                words_with_required_letters.append(word)

    # Print the count of words and each word that uses all required letters
    print(f"Number of words using all '{required_letters}': {len(words_with_required_letters)}")
    for word in words_with_required_letters:
        print(word)

# Example usage for 'aeiou'
count_words_with_required_letters('words.txt', 'aeiou')

# Example usage for 'aeiouy'
count_words_with_required_letters('words.txt', 'aeiouy')