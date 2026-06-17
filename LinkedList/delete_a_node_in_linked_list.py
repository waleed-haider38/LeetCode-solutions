# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void
        Do not return anything, modify node in-place instead.
        """

        # Copy the value of the next node into the current node.
        # This makes the current node appear as the next node.
        node.val = node.next.val

        # Skip the next node by updating the pointer.
        # Effectively removes the next node from the linked list.
        node.next = node.next.next