class Solution:
    def countGoodSubstrings(self, s: str) -> int:

        # This variable will store the number
        # of good substrings we find
        count = 0

        # We move through the string and check
        # every substring of size 3
        #
        # Example:
        # s = "xyzzaz"
        #
        # i = 0 → "xyz"
        # i = 1 → "yzz"
        # i = 2 → "zza"
        # i = 3 → "zaz"
        #
        # We stop at len(s) - 2 because we need
        # 3 characters in every window
        for i in range(len(s) - 2):

            # Check if all 3 characters are different
            #
            # s[i]       -> first character
            # s[i + 1]   -> second character
            # s[i + 2]   -> third character
            #
            # A good substring means:
            # no repeated characters
            if s[i] != s[i + 1] and \
               s[i] != s[i + 2] and \
               s[i + 1] != s[i + 2]:

                # If all characters are unique,
                # increase the count
                count += 1

        # Return total number of good substrings
        return count