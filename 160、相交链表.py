"""
先定义一个链表的实现

思路：
先计算两个链表的长度，假设链表A长于链表B。
这一点很重要：   让长链表的指针先走 |m - n| 步，这样剩下的部分长度就相同了。
然后同时遍历两个链表，直到找到相交的节点或两个链表都遍历结束。
"""
#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type headA, headB: ListNode
        :rtype: ListNode
        """
        # 初始化两个指针
        ptrA = headA
        ptrB = headB
        
        # 遍历两个链表，直到两个指针相遇或者都为None
        while ptrA != ptrB:
            # 如果ptrA到达链表A的末尾，跳转到链表B的头部
            ptrA = ptrA.next if ptrA else headB
            # 如果ptrB到达链表B的末尾，跳转到链表A的头部
            ptrB = ptrB.next if ptrB else headA
        
        # 如果两个指针相遇，则返回交点，否则返回None
        return ptrA
            

    
    

