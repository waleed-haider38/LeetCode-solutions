class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Initialize two pointers at the opposite ends of the list
        left = 0
        right = len(s) - 1
        
        # Continue swapping until the two pointers meet in the middle
        while left < right:
            # Temporarily store the left character before overwriting it
            swap = s[left]
            # Assign the right character to the left position
            s[left] = s[right]
            # Assign the stored left character to the right position
            s[right] = swap
            
            # Move the left pointer forward and the right pointer backward
            left += 1
            right -= 1