class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def rec(start, end):
            if start == end:
                return None
            mid = start
            node = start
            while node and node.next and node != end and node.next != end:
                node = node.next.next
                mid = mid.next

            t = TreeNode(mid.val)
            t.left = rec(start, mid)
            t.right = rec(mid.next, end)
            return t

        return rec(head, None)


def get_list(values):
    if not values or len(values) == 0:
        return None

    head = ListNode(values[0])
    node = head
    for i in range(1, len(values)):
        node.next = ListNode(values[i])
        node = node.next
    return head


def print_list(head):
    node = head
    while node:
        print(node.val)
        node = node.next


tree = Solution().sortedListToBST(get_list([1, 2, 3, 4, 5, 6]))
print(tree)
