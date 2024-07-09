cnt_letters = 0
cnt_words = 0
cnt_sentence = 0
index = 0
 

def read_text(prompt):
    while True:
        try:
            return input(prompt)
        except ValueError:
            pass

def count_letters(string):
    global cnt_letters
    cnt_letters = sum(1 for c in string if c.isalpha())
    print("Count of Letters : ", cnt_letters)

def count_words(string):
    global cnt_words
    temp_words = string.split() 
    cnt_words = len(temp_words)
    print("Count of words : ", cnt_words)

def count_sentences(string):
    global cnt_sentence
    ending = ("!", ".", "?")
    for ch in ending:
        cnt_sentence += len(string.split(ch)) - 1

    #temp_sentence = string.split(".")
    #count_sentence = len(temp_sentence-1)
    print(f"Count of Sentence : {cnt_sentence}")

def calculate_index():
    global cnt_letters
    global cnt_words
    global cnt_sentence
    L = (cnt_letters/cnt_words) * 100
    S = (cnt_sentence/cnt_words) * 100
    print(f"Value of L : {L}")
    print(f"Value of S : {S}")

    #index=0.0588×388.89−0.296×11.11−15.8≈8.76
    #index=0.0588×L−0.296×S−15.8
    formula = 0.0588 * L - 0.296 * S - 15.8
    print(f"Actual index is : {formula}")
    index = round(formula)
    print(f"Index is : {index}")
 
    if (index < 1 ):
        print("Before Grade 1")
        return 1

    elif (index >= 16):
        print("16+")

    else:
        print(f"Grade {index}")

def main():
    text = read_text("Enter the sentence: ")
    count_letters(text)
    count_words(text)
    count_sentences(text)
    calculate_index()

main()