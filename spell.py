from textblob import Word

def check_word_spelling(word):
    word_obj = Word(word)
    result = word_obj.spellcheck()

    if word == result[0][0]:
        print(f'Spelling of "{word}" is correct!')
    else:
        print(f'Spelling of "{word}" is not correct!')
        print(f'Correct spelling of "{word}": "{result[0][0]}" (with {result[0][1]} confidence).')

if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    words = sentence.split()

    for word in words:
        check_word_spelling(word)
