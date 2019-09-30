class Solution(object):
    def fix_head(self, head):
        new_head = ListNode(head.val - 1)
        new_head.next = head
        return new_head

    def deleteDuplicates(self, head):
        if head is None:
            return None
        head = self.fix_head(head)
        node = head
        new_head = None
        new_node = None

        node = head
        while node is not None:
            is_unique = True
            while node is not None and node.next is not None and node.val == node.next.val:
                node = node.next
                is_unique = False

            if not is_unique:
                node = node.next
            elif node is not None:
                if new_head is None:
                    new_head = ListNode(node.val)
                    new_node = new_head
                else:
                    new_node.next = ListNode(node.val)
                    new_node = new_node.next
                node = node.next

        return new_head.next
