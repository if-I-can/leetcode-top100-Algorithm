"""
这个题目给定的限制还是很重要的，就是说一定存在n个连续的自然数，只不过可能不按顺序在列表中排列，然后还额外多一个值是这n个数值中的一个。
"""

"""
然后下一个关键点就来了，就是经典的快慢指针法（类似于之前的环形链表，）
"""

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = nums[0]
        fast = nums[0]

        while True:     #第一次相遇  一是为了确定是否有环，二是为了给找入口做铺垫，即重置慢指针。
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow = nums[0]    ##  找到入口后，重置慢指针。
        while True:              # 第二次相遇  就是  
            slow = nums[slow]
            fast = nums[fast]
            if slow == fast:
                break
        return slow


tp = Solution()
print(tp.findDuplicate([1,2,3,4,5,4]))