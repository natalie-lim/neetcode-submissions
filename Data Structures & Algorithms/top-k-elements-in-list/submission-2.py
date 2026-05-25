class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        d = defaultdict(int)
        for i in nums:
            d[i] = d[i] + 1
        
        l = []
        for key, val in d.items():
            l.append([val, key])
        l.sort()

        res = []
        while len(res) < k:
            res.append(l.pop()[1])
        
        return res


        
            