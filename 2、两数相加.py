# #正确答案
# class ListNode(object):          #链表的定义，链表其实可以理解为一个字典，在面试的时候一般会把链表的定义丢给你，一般是一个value和一个next。
#     def __init__(self, val=0, next=None):  #链表相较于数组对于search能力比较强，不用去遍历整个数组。
#         self.val = val
#         self.next = next
#
# class Solution(object):
#     def addTwoNumbers(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         dummy_head = ListNode(0)  # 哑节点，方便返回结果
#         current = dummy_head
#         carry = 0  # 进位
#
#         while l1 or l2:  #看来while 是会遍历所有列表式的循环
#             # print(l1,l2)  #<__main__.ListNode object at 0x000002B93774DD90> <__main__.ListNode object at 0x000002B93774DBE0>运行后是其地址。
#             # 如果l1或l2已经遍历完，则对应的值为0
#             x = l1.val if l1 else 0
#             y = l2.val if l2 else 0
#             sum = carry + x + y  # 当前位的总和
#
#             carry = sum // 10  # 计算进位
#             current.next = ListNode(sum % 10)  # 当前位的节点
#             current = current.next
#
#             # 移动到下一个节点
#             if l1:
#                 l1 = l1.next
#             if l2:
#                 l2 = l2.next
#
#         # 最后一个进位
#         if carry > 0:
#             current.next = ListNode(carry)
#         return dummy_head.next
#
# 辅助函数：将列表转换为链表
# def list_to_linkedlist(lst):
#     dummy_head = ListNode(0)
#     current = dummy_head
#     for number in lst:
#         current.next = ListNode(number)
#         current = current.next
#     return dummy_head.next
#
# # 辅助函数：将链表转换为列表
# def linkedlist_to_list(node):
#     result = []
#     while node:
#         result.append(node.val)
#         node = node.next
#     return result
#
# # 测试代码
# l1 = list_to_linkedlist([2, 4, 3])
# l2 = list_to_linkedlist([5, 6, 4])
# res = Solution()
# result_node = res.addTwoNumbers(l1, l2)
# result = linkedlist_to_list(result_node)
# print(result)  # 输出应为 [7, 0, 8]

#练习
class ListNode(object):
    def __init__(self,val = 0,next = None):
        self.val = val
        self.next = next

def List_to_Linklist(list):
    link = ListNode(0)
    current = link
    for number in list:
        current.next = ListNode(number)
        current = current.next
    return link.next

def Linklist_to_List(link):
    list = []
    while link:
        list.append(link.val)
        link = link.next
    return list

class Solution(object):
    def addTwoNumbers(self,l1,l2):

        linklist3 = ListNode(0)
        linklist4 = linklist3
        jinwei = 0
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            all = val1 + val2 + jinwei
            zhengshu = all//10
            jinwei = zhengshu
            linklist4.next = ListNode(all%10)
            linklist4 = linklist4.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if jinwei ==1:
            linklist4.next = ListNode(jinwei)
            linklist4 = linklist4.next
        return linklist3.next





linklist1 = List_to_Linklist([9,9,9,8,8,8])
linklist2 = List_to_Linklist([5,6,4])


solution = Solution()
add_result_list = solution.addTwoNumbers(linklist1,linklist2)
result = Linklist_to_List(add_result_list)
print(result)
