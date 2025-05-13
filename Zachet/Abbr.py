def make_acronym(phrase):
    parts = phrase.split()
    letters = []
    for word in parts:
        if word and word[0].isalpha():
            letters.append(word[0].upper())
    return ''.join(letters)

print(make_acronym((input())))
