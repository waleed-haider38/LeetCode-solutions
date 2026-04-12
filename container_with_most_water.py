from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            # area calculate
            area = min(height[left], height[right]) * (right - left)
            
            # max update
            max_area = max(max_area, area)

            # pointer move
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
    
s = Solution()

area =s.maxArea([5,1,2,3,4,5,7])

print(area)