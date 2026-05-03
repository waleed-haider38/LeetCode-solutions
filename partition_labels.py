from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Store the last position of every character
        # Example: for "abac", last_index = {'a': 2, 'b': 1, 'c': 3}
        last_index = {}

        for i, ch in enumerate(s):
            last_index[ch] = i

        # Final answer: sizes of partitions
        result = []

        # start = starting index of current partition
        # end = farthest index this partition must reach
        start = 0
        end = 0

        for i, ch in enumerate(s):
            # Current character may appear later,
            # so extend the partition boundary if needed
            end = max(end, last_index[ch])

            # If current index reaches the boundary,
            # all characters of this partition are fully contained
            if i == end:
                # Partition size = end - start + 1
                result.append(end - start + 1)

                # Next partition starts after current one
                start = i + 1

        return result