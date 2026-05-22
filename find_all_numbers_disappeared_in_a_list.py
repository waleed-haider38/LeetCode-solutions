from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        # Convert the input array into a set
        # This allows O(1) average lookup time
        seen = set(nums)

        # Store all missing numbers here
        result = []

        # Numbers should exist from 1 to n
        # where n = length of the array
        for num in range(1, len(nums) + 1):

            # If current number is not present in the set,
            # it means the number is missing from the array
            if num not in seen:
                result.append(num)

        # Return all missing numbers
        return result