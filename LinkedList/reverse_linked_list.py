from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # 'prev' reversed list ka previous node track karega.
        # Initially koi previous node nahi hota.
        prev = None

        # Current pointer head se traversal start karega.
        curr = head

        # Jab tak list ke nodes available hain.
        while curr:

            # Next node ko temporarily save kar lo,
            # kyun ke next pointer ko change karne wale hain.
            temp = curr.next

            # Current node ka next pointer reverse kar do.
            # Ab current node previous node ki taraf point karega.
            curr.next = prev

            # Prev ko current node par move karo.
            # Yeh reversed list ka naya head ban jata hai.
            prev = curr

            # Original list ke next node par move karo.
            curr = temp

        # Loop ke end par 'prev' reversed linked list ka head hoga.
        return prev