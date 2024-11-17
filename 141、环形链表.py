# Definition for singly-linked list.
#如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。
# 为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
# 注意：pos 不作为参数进行传递 。仅仅是为了标识链表的实际情况。
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = head.next
        slow = head
        while fast and fast.next:
            if fast == head:
                return True
            fast = fast.next,next
            slow = slow.next
        return False


