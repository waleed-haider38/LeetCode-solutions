from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Step 1: Dictionary to store frequency of each number
        freq = {}

        # Step 2: Build frequency map
        # Key = number from array
        # Value = how many times it appears
        for num in nums:
            if num in freq:
                # If number already exists, increment its count
                freq[num] += 1
            else:
                # First time seeing this number, initialize count to 1
                freq[num] = 1

        # Step 3: Find the number that appears exactly once
        # Problem guarantees only one such number exists
        for num in freq:
            if freq[num] == 1:
                return num