from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        # Length of the array
        n = len(nums)

        # Store final answers
        # Default value is -1 because some elements
        # may not have a next greater element
        result = [-1] * n

        # Monotonic decreasing stack
        # We store indices in the stack
        stack = []

        # Traverse the array twice from right to left
        # This helps us handle the circular array
        for i in range(2 * n, -1, -1):

            # Convert index into circular index
            current_index = i % n

            # Remove all smaller or equal elements
            # because they can never be the next greater
            while stack and nums[stack[-1]] <= nums[current_index]:
                stack.pop()

            # If stack is not empty,
            # top of stack is the next greater element
            if stack:
                result[current_index] = nums[stack[-1]]

            # Push current index into stack
            stack.append(current_index)

        return result