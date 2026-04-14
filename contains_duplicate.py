from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # This is approach taking large time to solve the question
        # nums.sort()
        # print(nums)
        # for i in range(len(nums)-1):
        #     if nums[i] == nums[i+1]:
        #         return True
        # return False
        # In this approach we will use set
        seen = set(nums)
        return len(seen) != len(nums)
