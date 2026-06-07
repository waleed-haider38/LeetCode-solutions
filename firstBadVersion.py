# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:

        # Search space starts from version 1 to version n
        left = 1
        right = n

        # Continue searching while more than one candidate exists
        while left < right:

            # Find the middle version
            mid = (left + right) // 2

            # If mid is bad, the first bad version
            # could be mid itself or somewhere to its left
            if isBadVersion(mid):
                right = mid

            # If mid is good, the first bad version
            # must be on the right side
            else:
                left = mid + 1

        # When left == right, we have found
        # the first bad version
        return left