
# Exercise 4

# Write a function named uses_only that takes a word and a string of letters, and that returns 'True' if the word contains only letters in the list.
# Can you make a sentence using only the letters 'acefhlo'? Other than “Hoe alfalfa?”


def uses_only(word, string_of_letters):
    # Check if a word contains only letters from the specified string_of_letters. And Returns - True if all characters in the word are in the string_of_letters, False otherwise.
    for letter in word:
        if letter not in string_of_letters:
            return False
    return True


def words_from_letters(file_name, letters):
    """
    Find and print words from a file that contain only the specified letters.
    
    Parameters:
    - file_name: Name of the file containing words (one word per line).
    - letters: A string of letters to check against each word.
    
    Returns:
    - None (prints words directly).
    """
    list_of_words_from_letters = []
    
    # Open the file in read mode and Iterate through each line in the file
    with open(file_name, 'r') as File:
        for line in File:
            word = line.strip() # Strip any leading or trailing whitespace from the line
            # Check if the word uses only the specified letters. If it does, add it to the list of valid words
            if uses_only(word, letters):
                list_of_words_from_letters.append(word)
    
    # Print the list of words that use only the specified letters
    for word in list_of_words_from_letters:
        print(word)

words_from_letters('words.txt', 'acefhlo')

