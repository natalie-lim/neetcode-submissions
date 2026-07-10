class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d = {}

        for c in s1:
            if c in d:
                val = d[c]
                d[c] = val + 1
            else:
                d[c] = 1
        
        d_clone = d.copy()

        pt1 = 0
        pt2 = 0

        while pt2 <= (len(s2) - 1):
            print("pt1: ", pt1)
            print("pt2: ", pt2)

            c2 = s2[pt2]

            if c2 not in d_clone:
                print("not in")
                pt1_val = s2[pt1]

                if pt1_val in d:
                    if pt1_val in d_clone:
                        val = d_clone[pt1_val]
                        d_clone[pt1_val] = val + 1
                    else:
                        d_clone[pt1_val] = 1
                    pt2 -= 1

                pt1 += 1
                print(d_clone)

                
            else:
                val = d_clone[c2]
                if val-1 == 0:
                    del d_clone[c2]
                else:
                    d_clone[c2] = val - 1

            if len(d_clone) == 0:
                return True

            pt2 += 1

        return False