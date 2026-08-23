from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # 创建一个虚拟节点，指向链表的头部
        p0 = dummy = ListNode(next=head)
        # 找到第 left 个节点的前一个节点 p0
        for _ in range(left -1):
            p0 = p0.next
        # p1 指向第 left 个节点
        pre = None
        cur = p0.next
        # 反转从 p1 开始的 right - left + 1 个节点
        for _ in range(right - left +1):
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp

        # p0为left前一个指向反转完后的第一个pre
        # p0.next(head).next为left前一个指向反转完后的最后一个指向cur(即为反转完后的下一个节点)
        p0.next.next = cur
        p0.next = pre
        
        return dummy.next

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    left = 2
    right = 4

    solution = Solution()
    reversed_head = solution.reverseBetween(head, left, right)

    # Print the reversed linked list
    current = reversed_head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")