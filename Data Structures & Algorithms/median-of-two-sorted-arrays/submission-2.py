#nums1 = [1, 3, 8]
#nums2 = [7, 9, 10, 11]
# acc = [1, 3, 7, 8, 9, 10, 11]
# med = 8

#nums1 = [1, 2, 8]
#nums2 = [1, 3, 6, 7]
# acc = [1, 1, 2, 3, 6, 7, 8]

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A): # we set the smaller array to array A
            A, B = B, A

        l, r = 0, len(A) - 1 # 2 pointers for the smaller array

        while True: # loop indefinitely until we get the median
            i = (l + r) // 2 # middle of the smaller array
            j = half - i - 2 # partition index of the other array

            Aleft = A[i] if i >= 0 else float("-infinity") # left pt val of the array
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity") # the confirmation check value i think
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity") # the confirmation comparison

            if Aleft <= Bright and Bleft <= Aright: # if we've found the median
                if total % 2: # if ts even
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2

            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1

            
