class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 1. Setup tools
        char_map = {} # Our Memory Notebook
        left = 0
        max_len = 0
        
        # 2. Expand window with 'right' finger
        for right, char in enumerate(s):
            # 3. Conflict Check: Have we seen this letter before?
            if char in char_map:
                # 4. Jump the 'left' finger forward
                left = max(left, char_map[char] + 1)
            
            # 5. Record/Update the most recent position
            char_map[char] = right
            
            # 6. Update max_length of the current "clean" window
            max_len = max(max_len, right - left + 1)
            
        return max_len