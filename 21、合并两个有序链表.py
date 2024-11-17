class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(0)  # 创建一个哑节点
        current = dummy  # 指针指向新链表的最后一个节点

        while list1 and list2:  # 只要两个链表都有节点
            # print(list1.val)
            # print(list2.val)
            if list1.val <= list2.val:  # 比较两个链表当前节点的值
                current.next = list1  # 将较小的节点连接到新链表
                list1 = list1.next  # 移动 list1 指针
            else:
                current.next = list2  # 将较小的节点连接到新链表
                list2 = list2.next  # 移动 list2 指针
            current = current.next  # 移动到新链表的最后一个节点

        # 链接剩余的节点
        while list1:
            current.next = list1
            list1 = list1.next
            current = current.next
        while list2:
            print(list2.val)
            current.next = list2
            list2 = list2.next
            current = current.next

        return dummy.next  # 返回新链表的头节点

def list_to_linklist(list):
    res = ListNode(0)
    res_1 = res
    for i in list:
        res_1.next = ListNode(i)
        res_1 = res_1.next
    return res.next

def linklist_to_list(linklist):
    a = []
    while linklist:
        a.append(linklist.val)
        linklist = linklist.next
    return a

initial = Solution()
l1 = [1,2,3]
l2 = [2,3,4,5]
ll1 = list_to_linklist(l1)
ll2 = list_to_linklist(l2)
result = initial.mergeTwoLists(ll1,ll2)
# print(result)
