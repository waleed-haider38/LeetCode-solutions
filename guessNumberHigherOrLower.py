# The guess API is already defined for you.
# def guess(num: int) -> int:
# returns:
#  0 -> correct number
#  1 -> target is higher than num
# -1 -> target is lower than num

class Solution:
    def guessNumber(self, n: int) -> int:
        
        # Step 1: Define search space
        # The number is between 1 and n
        left = 1
        right = n

        # Step 2: Binary Search loop
        # Continue until search space is valid
        while left <= right:

            # Step 3: Find middle element
            # Safe formula to avoid overflow issues
            mid = left + (right - left) // 2

            # Step 4: Check guess result
            result = guess(mid)

            # Step 5: If correct number found
            if result == 0:
                return mid

            # Step 6: If guessed number is smaller than target
            # Move search to right half
            elif result == 1:
                left = mid + 1

            # Step 7: If guessed number is bigger than target
            # Move search to left half
            else:
                right = mid - 1