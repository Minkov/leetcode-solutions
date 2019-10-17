class Solution:
    def reverseBetween(self, head, m: int, n: int):
        reversed = head
        new_head = reversed
        for _ in range(m):
            reversed = reversed.next
        node = reversed.next
        reversed.next = None
        node = node.next

        while node:
            tmp = node
            node = node.next
            tmp.next = reversed
            reversed = tmp
        return new_head

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def list_to_linked_list(list):
    head = ListNode(-1)
    node = head
    for x in list:
        node.next = ListNode(x)
        node = node.next
    return head.next

def print_linked_list(head):
    while head:
        print(head.val)
        head = head.next

print_linked_list(
    Solution().reverseBetween(
        list_to_linked_list([1, 2, 3, 4, 5]),
        2, 4
    )
)