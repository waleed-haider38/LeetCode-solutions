class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        # 1. Create the "Target Notebook" for s1
        target_counts = {}
        for char in s1:
            target_counts[char] = target_counts.get(char, 0) + 1

        # 2. Create your "Window Notebook" for the first window of s2
        window_counts = {}
        k = len(s1)
        for i in range(k):
            window_counts[s2[i]] = window_counts.get(s2[i], 0) + 1

        # 3. Slide the window
        for i in range(k, len(s2)):
            # Check if we hit the jackpot!
            if window_counts == target_counts:
                return True
            
            # Welcome the new character
            char_in = s2[i]
            window_counts[char_in] = window_counts.get(char_in, 0) + 1
            
            # Goodbye to the old character
            char_out = s2[i - k]
            window_counts[char_out] -= 1
            if window_counts[char_out] == 0:
                del window_counts[char_out]

        # Final check for the last window
        return window_counts == target_counts