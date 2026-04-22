from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_number = nums[0]
        for i in nums:
            if i < min_number:
                min_number = i
        return min_number

        