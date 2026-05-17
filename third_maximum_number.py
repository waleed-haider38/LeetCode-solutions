from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:

        first = second = third = float('-inf')

        for num in nums:

            # skip duplicates
            if num == first or num == second or num == third:
                continue

            # new first maximum
            if num > first:
                third = second
                second = first
                first = num

            # new second maximum
            elif num > second:
                third = second
                second = num

            # new third maximum
            elif num > third:
                third = num

        # if third maximum doesn't exist
        if third == float('-inf'):
            return first

        return third