class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord in wordList:
            wordList.remove(beginWord)
        wordList.insert(0, beginWord)

        n = len(wordList) + 1
        adj = [[] for _ in range(n)]
        word_dict = {} # word, pos in endword
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
        'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


        # create word dict of the word: idx in the list
        for idx, word in enumerate(wordList):
            word_dict[word] = idx

        def findNeighbors(word):
            neighbors = []
            for idx, c in enumerate(word):
                for letter in alphabet:
                    new_word = word[0:idx] + letter + word[idx + 1:]
                    if new_word in word_dict and new_word != word:
                        neighbors.append(word_dict[new_word])
            
            return neighbors
        
        for idx, word in enumerate(wordList):
            adj[idx] = findNeighbors(word)

        discovered = [False] * n
        count = 0
                
        q = deque()
        q.append((0, 1)) # node, layer
        discovered[0] = True
        count = 0

        while q:
            n, l = q.pop()
            if wordList[n] == endWord:
                count = l
                break
            neighbors = adj[n]
            for node in neighbors:
                if not discovered[node]:
                    q.appendleft((node, l + 1))
                discovered[node] = True

        return count