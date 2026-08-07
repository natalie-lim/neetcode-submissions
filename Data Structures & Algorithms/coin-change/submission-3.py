class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        arr = []
        arr.append(0)
        for i in range(amount):
            arr.append(amount + 1)
        
        for amt in range(amount + 1):
            for c in coins:
                if amt - c >= 0:
                    arr[amt] = min(arr[amt], 1 + arr[amt-c])

        return arr[amount] if arr[amount] <= amount else -1