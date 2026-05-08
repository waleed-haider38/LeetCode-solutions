from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Finds the k most frequent elements in an array using Bucket Sort logic.
        Time Complexity: O(N)
        Space Complexity: O(N)
        """
        # Step 1: Count the frequency of each number using a Hash Map
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # Step 2: Create "Buckets" where the index represents the frequency.
        # Example: buckets[3] will hold all numbers that appeared 3 times.
        buckets = [[] for _ in range(len(nums) + 1)]
        
        for num, freq in count.items():
            buckets[freq].append(num)

        # Step 3: Collect the top k elements by walking through buckets backward.
        # We start from the highest possible frequency (the end of the list).
        result = []
        for i in range(len(buckets) - 1, 0, -1):
            # Check each number in the current frequency bucket
            for n in buckets[i]:
                result.append(n)
                # Once we've collected k numbers, we are done
                if len(result) == k:
                    return result