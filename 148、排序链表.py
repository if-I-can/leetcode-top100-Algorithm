# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        a = []
        while head:
            a.append(head.val)
            head =head.next
        a.sort()
        current = ListNode(0)
        b = current
        for i in a:
            res = ListNode(i)
            b.next = res
            b = b.next
        return current.next



