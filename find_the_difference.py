class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        freq_s = {}
        freq_t = {}

        # Count frequency in s
        for char in s:
            if char in freq_s:
                freq_s[char] += 1
            else:
                freq_s[char] = 1

        # Count frequency in t
        for char in t:
            if char in freq_t:
                freq_t[char] += 1
            else:
                freq_t[char] = 1

        # Compare frequencies
        for char in freq_t:
            if char not in freq_s or freq_s[char] != freq_t[char]:
                return char