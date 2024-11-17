#给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def swapPairs(self, head):
        dumpy = ListNode(0)
        dumpy.next = head
        pre = dumpy
        while pre.next and pre.next.next:
            # 确定第一个节点 和第二个节点
            first = pre.next
            second = pre.next.next

            #交换节点
            first.next = second.next
            second.next = first
            pre.next = second

            pre = first

        return dumpy.next
