class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        res = []
        subset = []

        def helper(i, curr_sum):
            if curr_sum == 0:
                res.append(subset.copy())
                return
            if i >= len(candidates) or candidates[i] > curr_sum:
                return
            
            curr_val = candidates[i]
            subset.append(curr_val)
            helper(i + 1, curr_sum - curr_val)
            subset.pop()
            idx = i + 1
            if idx < len(candidates):
                next_val = candidates[idx]
                while idx + 1 < len(candidates) and curr_val == next_val:
                    idx += 1
                    next_val = candidates[idx]
                if next_val != curr_val:
                    helper(idx, curr_sum)
           

        helper(0, target)
        return res
            