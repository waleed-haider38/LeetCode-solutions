from typing import Optional

# Definition for a singly-linked list node.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # Store visited nodes to detect if we revisit a node
        visited = set()

        # Start traversing from the head node
        current = head

        # Traverse the linked list until we reach the end
        while current:

            # If the current node has already been seen,
            # a cycle exists in the linked list
            if current in visited:
                return True

            # Mark the current node as visited
            visited.add(current)

            # Move to the next node
            current = current.next

        # If we reach None, there is no cycle
        return False