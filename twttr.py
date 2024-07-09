def get_vowels(str):
    vowels = "aeiouAEIOU"

    result = []
    for char in str:
        if char not in vowels:
            result.append(char)

    return ''.join(result)

def main():
    input_string = input("Input:")
    output_string = get_vowels(input_string)
    print("Output: ", output_string)

main()