def load_words(path):
    with open(path) as file:
        return [line.strip() for line in file]
