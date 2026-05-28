class Solution:
    def nextGreaterElement(self, nums1, nums2):

        stack = []

        # Store next greater element
        next_greater = {}

        # Traverse nums2 from right to left
        for i in range(len(nums2) - 1, -1, -1):

            current = nums2[i]

            # Remove smaller or equal elements
            while stack and stack[-1] <= current:
                stack.pop()

            # If stack not empty, top is next greater
            if stack:
                next_greater[current] = stack[-1]
            else:
                next_greater[current] = -1

            # Push current element
            stack.append(current)

        # Build answer for nums1
        result = []

        for num in nums1:
            result.append(next_greater[num])

        return result