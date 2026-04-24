from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # Iterate through each element in the array
        for i in nums:
            # If current element matches target, return True
            if i == target:
                return True
        
        # If loop completes and target not found
        return False