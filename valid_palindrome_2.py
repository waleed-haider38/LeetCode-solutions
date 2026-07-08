class Solution:
    def validPalindrome(self, s: str) -> bool:
        # Initialize two pointers at the start and end of the string
        left = 0
        right = len(s) - 1

        # Move pointers towards the center while they do not cross
        while left < right:
            # If a mismatch is detected, simulate deleting one character
            if s[left] != s[right]:
                # Option 1: Skip the character at the left pointer
                skipL = s[left + 1 : right + 1]
                # Option 2: Skip the character at the right pointer
                skipR = s[left : right]
                
                # Check if either remaining substring forms a valid palindrome
                return (skipL == skipL[::-1] or skipR == skipR[::-1])
            
            # Move pointers closer if the current characters match
            left += 1
            right -= 1
                    
        # Return True if the string is already a palindrome or can become one
        return True