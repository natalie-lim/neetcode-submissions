class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for i in strs:
            sort = "".join(sorted(i))
            if sort in d:
                d[sort].append(i)
            else:
                d[sort] = [i]
        
        l = []
        for key, val in d.items():
            l.append(val)
        
        return l