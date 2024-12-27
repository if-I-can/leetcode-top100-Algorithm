import heapq
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):  
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]                        ###这里还是蛮重要的，如果定义了像上面这样的ListNode 那传入的lists里面中的一个元素他的形式就是类似于 [1,listnode(3.listnode(4,listnode(5)))] 这种套娃形式的链表
        :rtype: Optional[ListNode]
        """
        new_lb = []
        for i in lists:
            if i:
                heapq.heappush(new_lb,(i.val,i))
        
        dumpy = ListNode()
        current = dumpy

        while new_lb:
            val,node = heapq.heappop(new_lb)   ##这里其实直接用占位符代替_也可以的     这里学习一个heapq这个包，还是有用的，尤其是升序链表。
            current.next = node           
            current = current.next
            if node.next:
                heapq.heappush(new_lb,(node.next.val,node.next))

        return dumpy.next