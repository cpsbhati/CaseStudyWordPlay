
## downlaod CROSSWD.TXT from https://www.gutenberg.org/files/3201/files/ and save it as word.txt

# Exercise 1  
# Write a program that reads 'words.txt' and prints only the words with more than 20 characters (not counting whitespace).

## Note to the reader I am still learning to code so my apologies for exesive use of comments.

def character_count(file_name):
    """
    Parameters:
    file_name (str): The name of the file to be read.
    """
    # Open the file in read mode
    fin = open(file_name)
    
    # Iterate over each line in the file
    for line in fin:
        # Remove leading and trailing whitespace characters from the line
        word = line.strip()
        
        # Check and pint the word if the length of the word is greater than 20 characters
        if len(word) > 20:
            print(word)
    
    # Close the file
    fin.close()

# Call the function with the specified file name
character_count('words.txt')
