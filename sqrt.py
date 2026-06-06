from math import sqrt , floor

class Solution:
    def mySqrt(self , x : int) -> int:
        low = 1 
        high = x

        while low <= high:

            mid = (low + high) // 2

            square = mid * mid

            if square == x:
                return mid
            elif square < x:
                low = mid + 1
            else:
                high = mid - 1
        return floor(sqrt(x))