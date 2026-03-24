import random
from utils.loader import load_words
from game.game import Game

def main():
    words = load_words("data/words.txt")
    solution = random.choice(words)

    game = Game(solution, words)

    while not game.is_over():
        guess = input("Ingresa palabra: ")
        
        try:
            result = game.guess(guess)
            print(result)
        except ValueError as e:
            print(e)

    if game.is_won():
        print("Ganaste")
    else:
        print(f"Perdiste. Era: {solution}")

if __name__ == "__main__":
    main()
