class Solution:
    def partition(self, s: str) -> List[List[str]]:

        res = []

        def isPalindrome(st, pt1, pt2):
            if len(st) <= 1:
                return True
            if pt1 >= pt2:
                return True
            c1 = st[pt1]
            c2 = st[pt2]
            if c1 != c2:
                return False
            return isPalindrome(st, pt1 + 1, pt2 - 1)


        def backtrack(i, subset, curr_str):
            if curr_str == "":
                res.append(subset.copy())
                return
            if i >= len(curr_str):
                return

            substr = curr_str[0: i+1]
            rest = curr_str[i + 1:]


            if isPalindrome(substr, 0, len(substr) - 1):                
                temp = subset.copy()
                temp.append(substr)
                backtrack(0, temp, rest)

            backtrack(i + 1, subset.copy(), curr_str)

        backtrack(0, [], s)
        return res