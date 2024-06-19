

# Exercise 6.
# Write a function called is_abecedarian that returns True if the letters in a word appear in alphabetical order (double letters are ok). 
# How many abecedarian words are there?

def is_abecedarian (word):
    # Check if the letters in a word appear in alphabetical order (double letters are ok)
    # Iterate through the characters in the word, starting from the second character
    for i in range(1, len(word)):
        # Compare the current character with the previous one
        if word[i] < word[i - 1]:
            return False
    return True 

# How many abecedarian words are there?
def find_abecedarian_word (filename):
    
    abecedarian_word_list = []

    # open the file and itrate over each line
    with open (filename, 'r') as fin:
        for line in fin:
            word = line.strip()
            if is_abecedarian(word):
                abecedarian_word_list.append(word)

    # count and print the words 
    print("Number of abecedarian words:", len(abecedarian_word_list))
    for word in abecedarian_word_list:
        print(f"{word:<20} Length: {len(word)}")

    # longest abecedarian word
    longest_abecedarian_word = ""
    for word in abecedarian_word_list:
        if len(word) >= len(longest_abecedarian_word):
            longest_abecedarian_word = word

    print(f"The longest abecedarian word is: {longest_abecedarian_word} and its lenght is {len(longest_abecedarian_word)}")


find_abecedarian_word('words.txt')
