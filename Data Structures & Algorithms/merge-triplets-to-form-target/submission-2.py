class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # if it can be one of the two keep and pair with another
        # if they match with one of these, put it in
        aset = set()
        bset = set()
        cset = set()

        target_a, target_b, target_c = target

        for triplet in triplets:
            if triplet == target:
                return True
            a, b, c = triplet
            if a == target_a and b <= target_b and c <= target_c:
                if len(bset) > 0 and len(cset) > 0:
                    return True
                aset.add(tuple(triplet))
            if b == target_b and a <= target_a and c <= target_c:
                if len(aset) > 0 and len(cset) > 0:
                    return True
                bset.add(tuple(triplet))
            if c == target_c and a <= target_a and b <= target_b:
                if len(aset) > 0 and len(bset) > 0:
                    return True
                cset.add(tuple(triplet))
        
        return False
