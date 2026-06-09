from typing import List

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        # Base Case: If total required flowers exceed the available flowers, it's impossible
        if m * k > len(bloomDay):
            return -1
        
        # Define search range: Minimum day possible to maximum day in the array
        left = min(bloomDay)
        right = max(bloomDay)
        ans = -1
        
        # Binary Search on the answer space (days)
        while left <= right:
            mid = (left + right) // 2
            
            # Check if it's possible to make 'm' bouquets by day 'mid'
            if self.canMakeBouquet(bloomDay, m, k, mid):
                ans = mid          # Save current mid as a valid answer
                right = mid - 1    # Try to find a smaller number of days (search left)
            else: 
                left = mid + 1     # Not enough bouquets, we need more days (search right)
                
        return ans

    # Helper function to check feasibility for a specific day (mid)
    def canMakeBouquet(self, bloomDay: List[int], m: int, k: int, mid: int) -> bool:
        flowers = 0
        bouquets = 0
        
        for day in bloomDay:
            if day <= mid:
                # Flower has bloomed by or on day 'mid', add to current adjacent chain
                flowers += 1
                
                # If we collected enough adjacent flowers for one bouquet
                if flowers == k:
                    bouquets += 1
                    flowers = 0  # Reset counter to start a new bouquet
            else:
                # Chain is broken because this flower hasn't bloomed yet
                flowers = 0
                
        # Return True if we managed to make at least the required 'm' bouquets
        return bouquets >= m