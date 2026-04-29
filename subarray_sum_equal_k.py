from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Dictionary to store frequency of prefix sums
        # Key: prefix sum, Value: how many times it has occurred
        prefix_count = {0: 1}

        # This keeps track of running sum while iterating array
        current_sum = 0

        # This stores total number of valid subarrays
        count = 0

        # Traverse through each number in the array
        for num in nums:
            # Add current number to running sum
            current_sum += num

            # Check if (current_sum - k) exists in prefix_count
            # If yes, it means there exists a subarray ending here with sum = k
            if current_sum - k in prefix_count:
                count += prefix_count[current_sum - k]

            # Store/update current prefix sum in dictionary
            prefix_count[current_sum] = prefix_count.get(current_sum, 0) + 1

        # Return total count of subarrays with sum equal to k
        return count