class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        # 1. Count vowels in the first window manually
        current_count = 0
        for i in range(k):
            if s[i] in vowels:
                current_count += 1
        
        # 2. Set our initial maximum
        max_vowels = current_count
        
        # 3. Slide the window
        for i in range(k, len(s)):
            # Add the new character at the front
            if s[i] in vowels:
                current_count += 1
            
            # Subtract the character that just left the back
            if s[i - k] in vowels:
                current_count -= 1
            
            # Update the record if we found more vowels
            if current_count > max_vowels:
                max_vowels = current_count
                
        return max_vowels