class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def to_array(self, head):
        node = head
        arr = []
        while node:
            arr.append(node)
            node = node.next
        return arr

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        nodes = self.to_array(head)
        stack = []
        def recursive(node, index):
            if not node:
                return index
            elif len(stack) == k:
                while stack:
                    nodes[index].val = stack.pop()
                    index += 1
            stack.append(node.val)
            return recursive(node.next, index)
        stack = []

        index = recursive(head, 0)

        if len(stack) == k:
            while stack:
                nodes[index].val = stack.pop()
                index += 1
        return head

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


# print_list(Solution().reverseKGroup(get_list([1, 2, 3, 4, 5]), 2))
# print_list(Solution().reverseKGroup(get_list([1, 2, 3, 4, 5]), 3))
print_list(Solution().reverseKGroup(get_list([]), 0))
print_list(Solution().reverseKGroup(get_list([1, 2]), 2))
