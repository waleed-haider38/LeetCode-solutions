from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Start traversing from the head of the linked list.
        current = head

        # Continue while both current node and next node exist.
        while current and current.next:

            # If the current node and next node have the same value,
            # a duplicate has been found.
            if current.val == current.next.val:

                # Remove the duplicate node by skipping it.
                current.next = current.next.next

            else:
                # Move to the next node when values are different.
                current = current.next

        # Return the head of the modified linked list.
        return head