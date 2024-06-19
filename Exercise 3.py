

# Exercise 3. Write a function named avoids that takes a word and a string of forbidden letters,and that returns True if the word doesn’t use any of the forbidden letters. 
# 
# Modify your program to prompt the user to enter a string of forbidden letters and then print the number of words that don’t contain any of them. 
# 
# Can you find a combination of 5 forbidden letters that excludes the smallest number of words?

def avoids(word, forbidden_letters):
    # Returns True if the word doesn't contain any forbidden letters, False otherwise.
    for letter in forbidden_letters:
        if letter in word:
            return False
        
    return True

def count_words_without_forbidden_letters(file_name, forbidden_letters):
    # count the number of words that does not contain forbidden letters
    count = 0 
    with open ( file_name, 'r' ) as file:
        for word in file:
            word = word.strip() # remove leading and trailing spaces.
            if( avoids( word, forbidden_letters) ):
                count += 1
    return count

# Prompt the user to enter forbidden letters
forbidden_letters = input("Enter forbidden letters: ")

# Call the function to count words without forbidden letters
count = count_words_without_forbidden_letters('words.TXT', forbidden_letters)

# Print the number of words without forbidden letters
print(f"Number of words without forbidden letters: {count}")
