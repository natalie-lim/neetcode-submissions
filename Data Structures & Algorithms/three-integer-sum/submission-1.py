class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        print(nums)
        output = []

        for idx, val in enumerate(nums):
            neg_num = val * -1
            pt1 = idx + 1
            pt2 = len(nums) - 1
            while (pt1 < pt2 and pt2 > idx):
                val1 = nums[pt1]
                val2 = nums[pt2]
                add = val1 + val2
                if (add == neg_num):
                    if not [val, val1, val2] in output:
                        output.append([val, val1, val2])
                    pt2 -= 1
                    pt1 += 1
                elif (add > neg_num):
                    pt2 -= 1
                else:
                    pt1 += 1

        return output


        