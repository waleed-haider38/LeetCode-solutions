class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        # Dictionary to store the frequency of prefix sums
        # Base case: A prefix sum of 0 has occurred exactly 1 time (before starting)
        prefix_sums = {0: 1}
        
        current_sum = 0
        total_subarrays = 0
        
        for num in nums:
            # Add the current number to the running total (Prefix Sum)
            current_sum += num
            
            # Check if (current_sum - k) exists in our hash map
            # If it exists, it means we found a valid subarray that sums up to k
            if (current_sum - k) in prefix_sums:
                total_subarrays += prefix_sums[current_sum - k]
            
            # Store/Update the count of the current prefix sum in the map
            if current_sum in prefix_sums:
                prefix_sums[current_sum] += 1
            else:
                prefix_sums[current_sum] = 1
                
        return total_subarrays