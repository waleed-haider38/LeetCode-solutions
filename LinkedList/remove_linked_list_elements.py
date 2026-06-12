from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        # Create a dummy node before the head.
        # This helps handle cases where the head itself
        # needs to be removed.
        dummy = ListNode(0)
        dummy.next = head

        # Start traversal from the dummy node.
        current = dummy

        # Continue until there are no more nodes ahead.
        while current.next:

            # If the next node contains the target value,
            # bypass it by updating the next pointer.
            if current.next.val == val:
                current.next = current.next.next

            # Otherwise, move to the next node.
            else:
                current = current.next

        # Return the updated head of the linked list.
        return dummy.next