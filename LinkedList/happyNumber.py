class Solution:
    def isHappy(self, n: int) -> bool:

        # Helper function:
        # This converts a number into "sum of squares of its digits"
        # Example: 19 → 1² + 9² = 82
        def next_number(n):
            total = 0

            # Extract digits one by one from right side
            while n > 0:
                digit = n % 10        # get last digit
                total += digit * digit  # square it and add
                n //= 10              # remove last digit

            return total  # return transformed number

        # Slow pointer starts from original number
        slow = n

        # Fast pointer also starts from original number
        fast = n

        # We keep looping until we either:
        # 1) reach 1 (happy number)
        # 2) detect a cycle (slow == fast)
        while True:

            # Move slow pointer by 1 transformation
            slow = next_number(slow)

            # Move fast pointer by 2 transformations
            # (fast moves faster to detect cycle early)
            fast = next_number(next_number(fast))

            # If fast reaches 1 → we found a happy number
            if fast == 1:
                return True

            # If slow and fast meet → cycle detected
            # meaning we are stuck in repeating loop → not happy
            if slow == fast:
                return False