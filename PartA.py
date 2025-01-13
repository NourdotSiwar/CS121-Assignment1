import re
import sys

'''
    This function tokenizes the content of a text file by reading it line by line, removing non-alphanumeric characters,
    and converting the text to lowercase. Valid tokens (alphanumeric words) are extracted and returned as a list.

    Runtime Complexity:
    - Opening the file runs in constant time O(1).
    - Reading each line in the file runs in O(n), where n is the number of lines in the file.
    - For each line, the regular expression `re.findall(r'[a-zA-Z0-9]+', line.lower())` scans through the entire line, which has a time complexity of O(m), where m is the length of the line.
    - The `extend()` function, which appends all tokens from the current line to the `tokens` list, runs in O(k), where k is the number of tokens in that line. Since tokens are proportional to the length of the line, this is at most O(m) for each line.
    
    Overall, if the file has a total length of `L` characters and `N` tokens, the complexity for tokenizing the entire file is O(L), where L is the total number of characters in the file (since we scan each character once).
    
    Therefore, the time complexity is linear with respect to the size of the input (O(L)), where L is total num of characters in the file.

'''
def tokenize(file_path):
    # init list of tokens
    tokens = []

    try:
        # Open file, read line by line
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                # Process each line by removing non-alphanumeric characters 
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

    return tokens


'''
    This function computes the frequency of each word (token) in the given list of tokens and returns a dictionary
    where the keys are the tokens and the values are the frequeencies of the tokens.

    Time Complexity:
    - The loop iterates through each token in the `tokens` list, which has `n` tokens.
    - For each token, checking whether it exists in the `frequencies` dictionary takes O(1) time on average (the average time complexity of dict lookups).
    - If the token is already in the dictionary, updating the frequency (`frequencies[token] += 1`) takes O(1) time.
    - If the token is not in the dictionary, adding the token to the dictionary (`frequencies[token] = 1`) also takes O(1) time on average.

    Overall, the function iterates over all tokens in the list once, performing constant-time operations for each token. Therefore, the time complexity is O(n), where `n` is the number of tokens in the `tokens` list.

'''
def computeWordFrequencies(tokens):
    # Init dictionary to store word frequencies
    frequencies = {}

    # Count the frequency of each word
    for token in tokens:
        if token in frequencies:
                frequencies[token] += 1
        else:
                frequencies[token] = 1
        
    return frequencies

'''
    This function prints the frequencies of words sorted by count in descending order. 
    In case of a tie, the words are sorted alphabetically in ascending order.

    Time Complexity:
    - Sorting the dictionary items using `sorted(frequencies.items(), key=lambda x: (-x[1], x[0]))`:
        - The `items()` method generates a list of dictionary items, which takes O(n) time, where n is the number of entries in the dictionary.
        - Sorting the list of items takes O(n log n) time, where n is the number of entries in the `frequencies` dictionary.
        - The sorting key `lambda x: (-x[1], x[0])` involves comparing the counts (`x[1]`) and resolving ties by comparing the words (`x[0]`), each comparison taking constant time. Therefore, sorting takes O(n log n) time.
    - Iterating over the sorted list to print the results:
        - The loop iterates over each item in the sorted list, which has O(n) time complexity.
        
    Overall, the dominant operation is the sorting step, which is O(n log n). Therefore, the time complexity is O(n log n), where n is the number of entries in the `frequencies` dictionary.
    
'''
def print_frequencies(frequencies):
    # Sort the dictionary by value in descending order (which is why x[1] is negated)
    # In case of a tie with counts, we resort to second value in the tuple which is x[0], sorting the words by alphabetic order
    sorted_frequencies = sorted(frequencies.items(), key=lambda x: (-x[1], x[0]))

    # Print sorted frequencies
    for token, count in sorted_frequencies:
        print(f"{token} - {count}")

    return

def main():
    if len(sys.argv) != 2:
        print("Usage command: python script.py <file_path>")
        sys.exit(1)  # Exit if the file path is not provided

    file_path = sys.argv[1]

    # Tokenize the file
    tokens = tokenize(file_path)

    # # Compute word frequencies
    frequencies = computeWordFrequencies(tokens)

    # # Print frequencies
    print_frequencies(frequencies)

if __name__ == "__main__":
    main()