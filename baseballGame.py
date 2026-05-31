from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:

        # Stack to store all valid scores
        stk = []

        # Process each operation one by one
        for op in operations:

            # "+" means add the last two valid scores
            if op == '+':
                stk.append(stk[-1] + stk[-2])

            # "D" means double the previous valid score
            elif op == 'D':
                stk.append(stk[-1] * 2)

            # "C" means remove the last valid score
            elif op == 'C':
                stk.pop()

            # Otherwise, the operation is a number
            # Convert it to integer and add it to the stack
            else:
                stk.append(int(op))

        # Return the sum of all remaining valid scores
        return sum(stk)