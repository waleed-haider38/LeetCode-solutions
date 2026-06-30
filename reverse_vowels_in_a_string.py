class Solution:
    def reverseVowels(self, s: str) -> str:
        # Define a set of vowels for O(1) fast lookup (both upper and lower case)
        vowels = set("aeiouAEIOU")
        
        # Convert string to a list because Python strings are immutable
        chars = list(s)
        
        left = 0
        right = len(chars) - 1
        
        while left < right:
            # Move left pointer forward if it's not pointing to a vowel
            while left < right and chars[left] not in vowels:
                left += 1
                
            # Move right pointer backward if it's not pointing to a vowel
            while left < right and chars[right] not in vowels:
                right -= 1
            
            # Both pointers are now at vowels; swap them using Pythonic assignment
            chars[left], chars[right] = chars[right], chars[left]
            
            # Move pointers inward to avoid an infinite loop
            left += 1
            right -= 1
            
        # Reconstruct the list back into a string
        return "".join(chars)