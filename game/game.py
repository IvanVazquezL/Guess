class Game:
    def __init__(self, solution, valid_words):
        self.solution = solution
        self.valid_words = set(valid_words)
        self.history = []
        self.max_turns = 6

    def guess(self, word):
        word = word.upper()

        if len(word) != 5:
            raise ValueError("Word must have 5 letters")

        if word not in self.valid_words:
            raise ValueError("Word is not valid")

        result = self._evaluate(word)

        self.history.append({
            "word": word,
            "result": result
        })

        return result
    
    def _evaluate(self, word):
        result = ["B"] * 5
        solution_chars = list(self.solution)

        for i in range(5):
            if word[i] == self.solution[i]:
                result[i] = "G"
                solution_chars[i] = None

        for i in range(5):
            if result[i] == "B" and word[i] in solution_chars:
                result[i] = "Y"
                #  consume only one ocurrence
                index = solution_chars.index(word[i])
                solution_chars[index] = None

        return result

    def is_won(self):
        if not self.history:
            return False

        return all(r == "G" for r in self.history[-1]["result"])

    def is_over(self):
        return self.is_won() or len(self.history) >= self.max_turns