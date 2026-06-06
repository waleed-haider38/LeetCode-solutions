class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # Search space: a square root of num must lie between 1 and num
        low = 1
        high = num

        while low <= high:
            # Find the middle value
            mid = (low + high) // 2

            # Calculate the square of mid
            square = mid * mid

            # Found an integer whose square equals num
            if square == num:
                return True

            # Current square is too small,
            # so search in the right half
            elif square < num:
                low = mid + 1

            # Current square is too large,
            # so search in the left half
            else:
                high = mid - 1

        # No integer square root was found
        return False