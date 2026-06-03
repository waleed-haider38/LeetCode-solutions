class Solution:
    def removeStars(self, s: str) -> str:
        # Stack to store characters after processing
        stk = []

        # Convert string into list of characters for iteration
        arr = list(s)

        # Traverse each character in the string
        for ch in arr:

            # If we encounter '*', we remove the last added character
            # This simulates "undo last operation"
            if ch == '*':
                stk.pop()

            else:
                # Otherwise, we push the character into the stack
                stk.append(ch)

        # Join all remaining characters to form final string
        return "".join(stk)