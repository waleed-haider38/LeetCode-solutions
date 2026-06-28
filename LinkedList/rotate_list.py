class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head or not head.next or k == 0:
            return head

        # Find length
        length = 1
        tail = head

        while tail.next:
            tail = tail.next
            length += 1

        # Reduce unnecessary rotations
        k %= length

        if k == 0:
            return head

        slow = head
        fast = head

        # Move fast k steps ahead
        for _ in range(k):
            fast = fast.next

        # Move together
        while fast.next:
            slow = slow.next
            fast = fast.next

        # Rotate
        new_head = slow.next
        slow.next = None
        fast.next = head

        return new_head