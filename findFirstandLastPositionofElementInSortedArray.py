from typing import List

from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        # Find the first occurrence of target
        def findFirst():
            left, right = 0, len(nums) - 1
            first = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    # Target found, save index
                    first = mid

                    # Continue searching on the left side
                    # to find an earlier occurrence
                    right = mid - 1

                elif nums[mid] < target:
                    # Target must be on the right side
                    left = mid + 1

                else:
                    # Target must be on the left side
                    right = mid - 1

            return first

        # Find the last occurrence of target
        def findLast():
            left, right = 0, len(nums) - 1
            last = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    # Target found, save index
                    last = mid

                    # Continue searching on the right side
                    # to find a later occurrence
                    left = mid + 1

                elif nums[mid] < target:
                    # Target must be on the right side
                    left = mid + 1

                else:
                    # Target must be on the left side
                    right = mid - 1

            return last

        # Return both boundaries
        return [findFirst(), findLast()]