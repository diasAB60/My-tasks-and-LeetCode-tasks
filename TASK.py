from typing import List
nums = [1, 15, 6, 3]
class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        SumOfElements = 0
        digits = 0
        SumOfDigits = 0
        for i in nums:
            SumOfElements += i
            while (i != 0):
                digits = i % 10
                i = i // 10
                SumOfDigits += digits
        return SumOfElements - SumOfDigits
print(Solution().differenceOfSum(nums))