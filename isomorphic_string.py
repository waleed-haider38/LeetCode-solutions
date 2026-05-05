class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        Determines if two strings are isomorphic using a character mapping strategy.
        Time Complexity: O(N) where N is the length of the string.
        Space Complexity: O(1) as the character set size is finite.
        """
        # Dictionary to store the unique mapping from characters in 's' to 't'
        notebook = {}
        # Set to ensure that no two characters in 's' map to the same character in 't'
        check_set = set()

        # Iterate through both strings simultaneously to build and verify mappings
        for char_s, char_t in zip(s, t):
            # Case 1: Character in 's' has been encountered before
            if char_s in notebook:
                # Validate that the existing mapping matches the current character in 't'
                if notebook[char_s] != char_t:
                    return False
            
            # Case 2: Character in 's' is new
            else:
                # Ensure the target character in 't' hasn't already been mapped to another letter
                if char_t in check_set:
                    return False
                
                # Establish the new character mapping and mark the target as used
                notebook[char_s] = char_t
                check_set.add(char_t)
        
        # All characters passed the one-to-one mapping criteria
        return True