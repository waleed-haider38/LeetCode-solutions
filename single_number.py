from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Finds the unique number in a list where every other number appears twice.
        Uses a Set to track numbers and remove pairs, leaving only the single number.
        Time Complexity: O(N)
        Space Complexity: O(N)
        """
        # A set to keep track of numbers we've seen only once
        check_set = set()

        for i in nums:
            # If the number is already in the set, we've found a pair
            if i in check_set:
                # Erase it from the set as we only care about unique numbers
                check_set.remove(i)
            else:
                # If it's new, add it to the 'tracking' notebook
                check_set.add(i)
        
        # After the loop, the only remaining number in the set is the one without a pair
        return check_set.pop()