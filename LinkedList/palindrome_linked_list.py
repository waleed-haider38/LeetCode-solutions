from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        # Create an empty list to store all node values
        values = []

        # Start traversing from the head node
        current = head

        # Traverse the linked list and collect values
        while current:
            values.append(current.val)
            current = current.next

        # Compare the list with its reversed version
        # If both are identical, the linked list is a palindrome
        if values == values[::-1]:
            return True

        # Otherwise, it is not a palindrome
        return False