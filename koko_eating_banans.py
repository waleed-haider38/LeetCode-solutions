from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # Helper function: calculates total hours needed for a given speed k
        def canFinish(k):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)  # important: ceil division
            return hours <= h
        
        # Search space for k
        left, right = 1, max(piles)
        
        # Binary search
        while left < right:
            mid = (left + right) // 2
            
            if canFinish(mid):
                right = mid   # try smaller speed
            else:
                left = mid + 1  # need higher speed
        
        return left