cnt_letters = 0
cnt_words = 0
cnt_sentence = 0

def read_text(prompt):
    while True:
        try:
            return input(prompt)
        except ValueError:
            pass

def count_letters(string):
    global cnt_letters
    cnt_letters = sum(1 for c in string if c.isalpha())
    print("Count of Letters: ", cnt_letters)

def count_words(string):
    global cnt_words
    temp_words = string.split() 
    cnt_words = len(temp_words)
    print("Count of Words: ", cnt_words)

def count_sentences(string):
    global cnt_sentence
    ending = ("!", ".", "?")
    for ch in ending:
        cnt_sentence += len(string.split(ch)) - 1
    print(f"Count of Sentences: {cnt_sentence}")

def main():
    text = read_text("Enter the sentence: ")
    count_letters(text)
    count_words(text)
    count_sentences(text)
    print(f"Inside main: Words: {cnt_words}, Letters: {cnt_letters}, Sentences: {cnt_sentence}")

    L = (cnt_letters / cnt_words) * 100  # Average number of letters per word
    S = (cnt_sentence / cnt_words) * 100  # Average number of sentences per word

    formula = (0.0588 * L) - (0.296 * S) - 15.8
    print(f"Formula is: {formula}")

main()
