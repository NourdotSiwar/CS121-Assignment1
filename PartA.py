import re
import sys


'''
Method/Function: List<Token> tokenize(TextFilePath)
Write a method/function that reads in a text file and returns a list of the tokens in that file. For the purposes of this project, a token is a sequence of alphanumeric characters, independent of capitalization (so Apple, apple, aPpLe are the same token). You are allowed to use regular expressions if you wish to (and you can use some regexp engine, no need to write it from scratch), but you are not allowed to import a tokenizer (e.g. from NLTK), since you are being asked to write a tokenizer.
'''
def tokenize(file_path):
    # init list of tokens
    tokens = []

    try:
        # Open file, read line by line
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                # Process each line by removing non-alphanumeric characters and splitting into words
                # Convert to lowercase for case insensitivity
                line_tokens = re.findall(r'[a-zA-Z0-9]+', line.lower())

                # Append valid tokens to the list
                tokens.extend(line_tokens)
                
        # Handle the case of an empty file (tokens would be an empty list)
        if not tokens:
            print("No tokens found. The file is empty or contains no valid tokens.")
        
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)  # Exit gracefully on error

    print(f"tokens: {tokens}")
    return tokens

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <file_path>")
        sys.exit(1)  # Exit if the file path is not provided

    file_path = sys.argv[1]

    # Tokenize the file
    tokens = tokenize(file_path)

    # # Compute word frequencies
    # frequencies = computeWordFrequencies(tokens)

    # # Print frequencies
    # print_frequencies(frequencies)

if __name__ == "__main__":
    main()


'''
Method/Function:        Map<Token,Count> computeWordFrequencies(List<Token>)
Write another method/function that counts the number of occurrences of each token in the token list. Remember that you should write this assignment yourself from scratch, so you are not allowed to import a counter when the assignment asks you to write that method.
'''
def computeWordFrequencies(tokens):
    

'''
Method/Function:         void print(Frequencies<Token, Count>)
Finally, write a method/function that prints out the word frequency count onto the screen. The printout should be ordered by decreasing frequency (so, the highest frequency words first; if necessary, order the cases of ties alphabetically). 
'''
def print(frequencies):
    pass

