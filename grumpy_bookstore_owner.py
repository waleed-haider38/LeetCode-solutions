class Solution:
    def maxSatisfied(self, customers, grumpy, minutes):

        # Customers already satisfied when owner is not grumpy
        satisfied = 0

        # Extra customers we can satisfy using the secret technique
        extra = 0

        # Maximum extra customers found in any window
        max_extra = 0

        left = 0

        for right in range(len(customers)):

            # If owner is NOT grumpy,
            # these customers are already satisfied
            if grumpy[right] == 0:
                satisfied += customers[right]

            # If owner IS grumpy,
            # these customers can become satisfied
            # if we use the technique here
            else:
                extra += customers[right]

            # Keep window size equal to "minutes"
            if right - left + 1 > minutes:

                # Remove left side of window
                # only if owner was grumpy there
                if grumpy[left] == 1:
                    extra -= customers[left]

                left += 1

            # Store best possible extra customers
            max_extra = max(max_extra, extra)

        # Total satisfied customers
        return satisfied + max_extra