from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        # Helper function: given capacity, kitne din lagenge?
        def canShip(capacity):
            d = 1
            total = 0
            
            for w in weights:
                if total + w > capacity:
                    d += 1
                    total = 0
                total += w
            
            return d <= days
        
        # Search space
        left = max(weights)      # minimum possible capacity
        right = sum(weights)     # maximum possible capacity
        
        # Binary search
        while left < right:
            mid = (left + right) // 2
            
            if canShip(mid):
                right = mid      # try smaller capacity
            else:
                left = mid + 1   # need more capacity
        
        return left