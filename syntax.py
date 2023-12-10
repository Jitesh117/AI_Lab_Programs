import nltk

def check_syntax(sentence):
    tokens = nltk.word_tokenize(sentence)
    pos_tags = nltk.pos_tag(tokens)
    return pos_tags

def analyze_syntax(pos_tags):
    mistakes = []
    for i in range(len(pos_tags)):
        word, pos = pos_tags[i]
        if pos not in ['NN', 'VB', 'JJ', 'DT', 'IN', 'RB']:
            mistakes.append((word, pos, i))
    return mistakes

def correct_sentence(sentence, mistakes):
    # Simple rule-based corrections (replace with your own rules)
    corrections = {
        'wanna': 'want to',
        'gonna': 'going to',
        'gotta': 'have to',
        'aint': 'am not',
        'dont': 'do not',
        'doesnt': 'does not'
    }

    corrected_words = []
    for word, pos, _ in mistakes:
        corrected_words.append(corrections.get(word.lower(), word))

    # Replace mistakes with corrections
    corrected_sentence = sentence
    for i in range(len(mistakes)):
        word, _, index = mistakes[i]
        corrected_sentence = corrected_sentence.replace(word, corrected_words[i])

    return corrected_sentence

# Example usage
if __name__ == "__main__":
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')

    sentence = input("Enter an English sentence for syntax checking: ")
    pos_tags = check_syntax(sentence)

    print("Part-of-speech tags:")
    print(pos_tags)

    mistakes = analyze_syntax(pos_tags)
    if mistakes:
        print("Potential mistakes:")
        for word, pos, _ in mistakes:
            print(f"- Word: {word}, Part of Speech: {pos}")

        corrected_sentence = correct_sentence(sentence, mistakes)
        print("Corrected sentence:")
        print(corrected_sentence)
    else:
        print("No potential mistakes found.")
