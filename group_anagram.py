from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Groups words that are anagrams of each other.
        Time Complexity: O(N * K log K) where N is the number of strings and K is max length.
        Space Complexity: O(N * K) to store the grouped strings.
        """
        # Create a dictionary where each key automatically starts with an empty list.
        # This prevents 'KeyErrors' when we encounter a new anagram pattern.
        notebook = defaultdict(list)

        for word in strs:
            # Anagrams share the same letters. By sorting them, they all 
            # produce the same 'key' (e.g., 'eat', 'tea', 'ate' all become 'aet').
            key = "".join(sorted(word))
            
            # Store the original word under its sorted 'canonical' key.
            notebook[key].append(word)
        
        # Return only the values (the lists of grouped anagrams) from our notebook.
        return list(notebook.values())