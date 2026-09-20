class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list) # sorted, list of words

        for word in strs:
            sor = ''.join(sorted(word))
            if sor in d:
                d[sor].append(word)
            else:
                d[sor] = [word]

        res = []
        for key, val in d.items():
            res.append(val)

        return res
