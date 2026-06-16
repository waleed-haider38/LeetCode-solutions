
class Solution:
    def getIntersectionNode(self, headA, headB):

        # Create a set to store all nodes from Linked List A
        visited = set()

        # Traverse Linked List A and add each node
        # to the set for O(1) lookup later
        current = headA
        while current:
            visited.add(current)
            current = current.next

        # Traverse Linked List B
        current = headB
        while current:

            # If the current node already exists in the set,
            # it means both lists share this exact node,
            # so we have found the intersection point
            if current in visited:
                return current

            current = current.next

        # No intersection found
        return None