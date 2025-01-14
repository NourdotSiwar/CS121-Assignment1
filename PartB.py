import sys
from PartA import tokenize, computeWordFrequencies, print_frequencies

'''
    This function finds common tokens between two files.

    Runtime Complexity:
    The function iterates over the keys in the first frequency dictionary (`frequencies1`) and checks for their existence in the second dictionary (`frequencies2`). If `n` is the size of `frequencies1` and `m` is the size of `frequencies2`, this operation is O(n) in the average case due to dictionary lookups being O(1) thus it would take O(1) to lookup the token in `frequencies2`

    Therefore, the overall complexity is O(n + m), considering the tokenization and frequency computation steps for both files.

'''
def findCommonTokens(file_path1, file_path2):

    # Get list of tokens from file_path1
    tokens1 = tokenize(file_path1)
    # Get frequency dictionary from the list of tokens produced from file_path1
    frequencies1 = computeWordFrequencies(tokens1)

    # Get list of tokens from file_path2
    tokens2 = tokenize(file_path2)
    # Get frequency dictionary from the list of tokens produced from file_path2
    frequencies2 = computeWordFrequencies(tokens2)

    # Keeping a counter of common tokens
    common_tokens = 0

    # Keeping a list of common tokens (optional)
    # common_tokens_list = []

    # Going through first dictionary and checking if the token exists in second dictionary
    for token in frequencies1:
        if token in frequencies2:
            # Increasing counter
            common_tokens += 1
            # common_tokens_list.append(token)

      
    # print out the common words
    # print(common_tokens_list)

    # print number of tokens they have in common
    print(common_tokens)

def validate_file(file_path):
    try:
        with open(file_path, "r") as file:
            return True
    except Exception as e:
        print(f"Error reading file: {e}")
        return False
    

def main():
    if len(sys.argv) != 3:
        print("Usage command: python script.py <file_path1> <file_path2>")
        sys.exit(1)  # Exit if the file path is not provided

    file_path1 = sys.argv[1]
    file_path2 = sys.argv[2]

    # validate file 1
    if not validate_file(file_path1):
        print("Invalid file path provided.")
        sys.exit(1)  # Exit if the file is invalid

    if not validate_file(file_path2):
        print("Invalid file path provided.")
        sys.exit(1)
    


    findCommonTokens(file_path1, file_path2)



if __name__ == "__main__":
    main()
