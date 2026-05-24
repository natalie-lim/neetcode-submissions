class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        print(c)
        idx = 0
        l = []
        for element, count in c.most_common():
            if idx >= k:
                break;
            l.append(element)
            idx += 1

        return l