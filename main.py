import random
from utils.loader import load_words

def main():
    words = load_words("data/words.txt")
    solution = random.choice(words)

if __name__ == "__main__":
    main()
