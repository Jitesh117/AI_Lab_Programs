from textblob import Word

def check_word_spelling(word):
    word_obj = Word(word)
    suggestions = word_obj.spellcheck()

    if word == suggestions[0][0]:
        print(f'Spelling of "{word}" is correct!')
    else:
        print(f'Spelling of "{word}" is not correct!')
        print(f'Suggested spellings for "{word}":')
        for suggestion in suggestions:
            print(f'  - "{suggestion[0]}" (confidence: {suggestion[1]})')

if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    words = sentence.split()

    for word in words:
        check_word_spelling(word)
