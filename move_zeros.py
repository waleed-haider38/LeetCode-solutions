from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        inserted_pos = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[inserted_pos] = nums[i]
                inserted_pos += 1

        for i in range(inserted_pos , len(nums)):
            nums[i] = 0

