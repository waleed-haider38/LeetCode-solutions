from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # Initialize the search range
        left = 0
        right = len(letters) - 1

        # Binary Search to find the first letter greater than target
        while left <= right:
            mid = (left + right) // 2

            # If the current letter is less than or equal to target,
            # the answer must be on the right side
            if letters[mid] <= target:
                left = mid + 1

            # Current letter is a valid candidate,
            # but there may be a smaller valid answer on the left
            else:
                right = mid - 1

        # If left moves beyond the last index,
        # no letter greater than target exists.
        # The problem requires wrapping around to the first letter.
        if left == len(letters):
            return letters[0]

        # left points to the smallest letter greater than target
        return letters[left]