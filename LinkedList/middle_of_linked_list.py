from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize both pointers at the head of the linked list
        slow = head
        fast = head
        
        # Traverse the list. 
        # We need to ensure 'fast' is not null and 'fast.next' is not null 
        # so that 'fast' can safely move two steps ahead.
        while fast and fast.next:
            slow = slow.next       # Move slow pointer 1 step
            fast = fast.next.next  # Move fast pointer 2 steps
            
        # When fast reaches the end, slow is at the middle node
        return slow