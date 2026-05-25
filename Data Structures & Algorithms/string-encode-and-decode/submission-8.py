class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            length = len(s)
            encoded += (str(length) + "#" + s)
        return encoded

    def decode(self, s: str) -> List[str]:
        l = []

        while (s.find("#") != -1):
            pound_idx = s.find("#")
            num_str = (s[:pound_idx])
            num = int(num_str)
            l.append(s[pound_idx + 1 :  (pound_idx + 1 + num)])
            s = s[pound_idx + 1 + num:]

        return l

