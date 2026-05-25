class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            length = len(s)
            encoded += (str(length) + "#" + s)
        return encoded

    def decode(self, s: str) -> List[str]:
        print(s)
        l = []
        curr_str = ""
        curr_num = 0
        num_str = ""
        for idx, c in enumerate(s):
            curr_str += c
            curr_num -= 1
            if (c == "#" and num_str != ""):
                curr_num = int(num_str)
                num_str = ""
                curr_str = ""
            try:
                int(c)
                num_str += c
            except:
                pass

            if (curr_num == 0):
                l.append(curr_str)
                num_str = ""
        
        return l
                


