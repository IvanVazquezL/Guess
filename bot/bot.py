class Bot:
    def __init__(self, words, strategy = None):
        self.all_words = words
        self.candidates = words.copy()

        if strategy is None:
            self.strategy = ["COMET", "FLASH", "BRINK", "PUDGY"]
        else:
            self.strategy = strategy

    def next_guess(self, history):
        turn = len(history)

        if turn < len(self.strategy):
            return self.strategy[turn]

        self.candidates = self.filter_candidates(history)

        if len(self.candidates) == 0:
            return self.all_words[0]

        if len(self.candidates) <= 2:
            return self.candidates[0]

        return self.select_best(self.candidates)

    def filter_candidates(self, history):
        candidates = self.all_words

        for entry in history:
            word = entry["word"]
            result = entry["result"]

            candidates = [
                w for w in candidates
                if self._matches(w, word, result)
            ]

        return candidates

    def _matches(self, candidate, word, result):
        temp = list(candidate)

        for i in range(5):
            if result[i] == "G":
                if candidate[i] != word[i]:
                    return False
                temp[i] = None

        for i in range(5):
            if result[i] == "Y":
                if word[i] not in temp:
                    return False
                index = temp.index(word[i])
                temp[index] = None

        for i in range(5):
            if result[i] == "B":
                if word[i] in candidate:
                    return False

        return True

    def select_best(self, candidates):
        freq = {}

        for word in candidates:
            for c in set(word):
                freq[c] = freq.get(c, 0) + 1

        best = None
        best_score = -1

        for word in candidates:
            score = sum(freq[c] for c in set(word))

            if score > best_score:
                best_score = score
                best = word

        return best