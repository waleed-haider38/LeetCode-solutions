from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(
        self,
        head: Optional[ListNode],
        left: int,
        right: int
    ) -> Optional[ListNode]:

        if not head or left == right:
            return head

        # Dummy node handles edge cases
        dummy = ListNode(0)
        dummy.next = head

        # Move prev to the node before 'left'
        prev = dummy
        for _ in range(left - 1):
            prev = prev.next

        # Start reversing
        current = prev.next

        for _ in range(right - left):
            temp = current.next
            current.next = temp.next
            temp.next = prev.next
            prev.next = temp

        return dummy.next