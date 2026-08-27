class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        app = []
        rev = reversed(num2)
        num1 = int(num1)

        for i, n in enumerate(rev):
            num = int(n)
            app.append(num * num1 * 10 ** i)

        res = 0
        for num in app:
            res += num

        return str(int(res))