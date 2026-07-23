class PrefixTree:

    def __init__(self):
        self.d = {}
        

    def insert(self, word: str) -> None:
        relevant_d = self.d
        for c in word:
            if c in relevant_d:
                relevant_d = relevant_d[c]
            else: 
                relevant_d[c] = {}
                relevant_d = relevant_d[c]
        relevant_d["$"] = {}

    def search(self, word: str) -> bool:
        relevant_d = self.d
        for c in word:
            if c not in relevant_d:
                return False
            relevant_d = relevant_d[c]
        if "$" in relevant_d:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        relevant_d = self.d
        for c in prefix:
            if c not in relevant_d:
                return False
            relevant_d = relevant_d[c]
        return True
        