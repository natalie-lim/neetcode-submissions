class WordDictionary:

    def __init__(self):
        self.d = {}

    def addWord(self, word: str) -> None:
        relevant_d = self.d
        for c in word:
            if c in relevant_d:
                relevant_d = relevant_d[c]
            else:
                relevant_d[c] = {}
                relevant_d = relevant_d[c]

        relevant_d["$"] = {}
        
    def _search_helper(self, word, idx, relevant_d):
        if idx >= len(word):
            return "$" in relevant_d
        c = word[idx]
        if c == ".":
            for d in relevant_d.values():
                if self._search_helper(word, idx + 1, d):
                    return True
            return False
        else:
            if c not in relevant_d:
                return False
            else:
                return self._search_helper(word, idx + 1, relevant_d[c])

    def search(self, word: str) -> bool:
        return self._search_helper(word, 0, self.d)