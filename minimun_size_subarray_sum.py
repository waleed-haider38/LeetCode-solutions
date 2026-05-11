from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # 1. Setup our tools
        left = 0
        current_sum = 0
        # Start with a "huge" number so any real length will be smaller
        min_length = float('inf') 
        
        # 2. Start expanding the window (Right Finger)
        for right in range(len(nums)):
            current_sum += nums[right]
            
            # 3. If target is hit, start shrinking (Left Finger)
            while current_sum >= target:
                # Calculate current window size: (right - left + 1)
                min_length = min(min_length, right - left + 1)
                
                # Throw away the back number to see if we can still hit the target
                current_sum -= nums[left]
                left += 1
                
        # 4. Final Check: Did we ever hit the target?
        return min_length if min_length != float('inf') else 0