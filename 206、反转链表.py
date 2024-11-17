#给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dumpy = ListNode(0)
        dumpy.next = head
        current = dumpy
        output =current
        a = []
        while dumpy.next:
            a.append(dumpy.next.val)
            dumpy =dumpy.next
        for i in a[::-1]:
            current.next = ListNode(i)
            current = current.next
        return output.next
