class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        d = {} # val, freq

        for h in hand:
            if h in d:
                prev = d[h]
                d[h] = prev + 1
            else:
                d[h] = 1
        
        d = dict(sorted(d.items()))

        for key, val in d.items():
            for i in range(val):
                d[key] = val - 1
                for k in range(groupSize - 1):
                    if not k + key + 1 in d:
                        return False
                    prev = d[k + key + 1]
                    d[k + key + 1] = prev - 1
        # for key, val in d.items():
        #     if val != 0:
        #         return False
        return True