# Exercise 2

# In 1939 Ernest Vincent Wright published a 50,000 word novel called Gadsby that does not contain the letter “e.” Since “e” is the most common letter in English, that’s not easy to do.
# In fact, it is difficult to construct a solitary thought without using that most common symbol. It is slow going at first, but with caution and hours of training you can gradually gain facility.
# All right, I’ll stop now.

# Write a function called has_no_e that returns 'True' if the given word doesn’t have the letter “e” in it.
# Modify your program from the previous section to print only the words that have no “e” and compute the percentage of the words in the list have no “e.”

def has_no_e( word ):
    # This funcation retruns 'True' if the word does not have 'e' in it.
    if 'e' not in word:
        return True
    else:
        return False

def process_words_list( file_name ):

    # open the file and read the lines (words) from it
    # note: in the file each line only has one word only 
    with open( file_name, 'r' ) as file_object: # Use 'with' to ensure the file is properly closed after we're done with it
        word_list = file_object.readlines()

    # total number of words 
    total_words = len( word_list )
    words_without_e = [] # list to store words without e

    # check each word and add it to the list if it doesn't have 'e' in it.
    for word in word_list:
        word = word.strip() # remove leading and trailing space
        if has_no_e( word ): # add word to the list if it doesn't have 'e' in it.
            words_without_e.append( word )
    
    # print words without 'e'
    for word in words_without_e:
        print( word )


    # compute the percentage of words without 'e'
    num_words_without_e = len( words_without_e )
    percentage_without_e = ( num_words_without_e / total_words ) * 100

    # print percentage 
    print( f"Percentage of words without 'e': {percentage_without_e: .2f}%" )

process_words_list( 'words.TXT' )