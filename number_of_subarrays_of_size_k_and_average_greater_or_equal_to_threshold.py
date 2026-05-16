from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # 1. The Target (sum must be >= target_sum)
        target_sum = threshold * k
        
        # 2. Initial Sum (First window lap)
        current_sum = sum(arr[:k])
        count = 0
        
        # 3. Check the very first window before sliding
        if current_sum >= target_sum:
            count += 1
            
        # 4. The Slide (Start from index k)
        for i in range(k, len(arr)):
            # Update sum: Add the new (i), remove the old (i-k)
            current_sum += arr[i] - arr[i-k]
            
            # Check the new window
            if current_sum >= target_sum:
                count += 1