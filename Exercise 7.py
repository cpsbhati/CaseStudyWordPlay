# Exercise 7
# This question is based on a Puzzler that was broadcast on the radio program Car Talk[2]:

# Give me a word with three consecutive double letters. I'll give you a

# couple of words that almost qualify, but don't. For example, the word committee, c-o-m-m-i-t-t-e-e. It would be great except for the ‘i’ that sneaks in there. Or Mississippi: M-i-s-s-i-s-s-i-p-p-i. If you could take out those i’s it would work. But there is a word that has three consecutive pairs of letters and to the best of my knowledge this may be the only word. Of course there are probably 500 more but I can only think of one. What is the word?

# Write a program to find it. You can see my solution at 'thinkpython.com/code/cartalk.py'.

## solution find word with three consicutive dobule letters.


def is_triple_double(word):
    # This function checks if a word contains three consecutive double letters
    count = 0  # Initialize a counter to keep track of consecutive double letters
    i = 0  # Initialize the index variable to start at the beginning of the word
    
    while i < len(word) - 1:  # Loop through the word until the second last character
        if word[i] == word[i + 1]:  # Check if the current character and the next character are the same
            count += 1  # Increment the counter if a double letter is found
            i += 2  # Move past this pair of double letters by incrementing the index by 2
            # Check if three consecutive double letters have been found
            if count == 3:
                return True  # Return True if found
        else:
            count = 0  # Reset the counter if the characters are not the same
            i += 1  # Move to the next character
    
    return False  # Return False if three consecutive double letters are not found

def find_triple_double(filename):
    # This function finds all words in a file that contain three consecutive double letters
    triple_doubles = []  # Empty list to store words with triple double letters

    # Open the file in read mode
    with open(filename, 'r') as fin:
        for line in fin:  # Loop through each line in the file
            word = line.strip()  # Strip leading and trailing whitespace from the word
            if is_triple_double(word):  # Check if the word contains three consecutive double letters
                triple_doubles.append(word)  # Add the word to the list if it does

    # Print each word that contains three consecutive double letters
    for word in triple_doubles:
        print(word)

# Example usage
find_triple_double('words.TXT')  # Call the function with the filename 'words.TXT'



