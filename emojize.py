# emojize.py

import emoji

def main():
    # Prompt the user for a string in English with emoji aliases
    user_input = input("Input: ")

    # Convert the aliases in the input to corresponding emoji
    emojized_str = emoji.emojize(user_input, language='alias')

    # Output the emojized version of the input string
    print("Output:", emojized_str)

if __name__ == "__main__":
    main()