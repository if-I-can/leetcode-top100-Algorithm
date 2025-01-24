"""
贪心算法，维护一个最大距离max_reach
1、max_reach是否允许达到挡墙节点: if max_reach > i
2、如果能到达i那，考虑下一步:维护新的max_reach
3、遍历nums中的所有元素，当存在一个max_rach大于n-1，则为True，否则为False

"""

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_reach = 0

        for i in range(len(nums)):
            if i > max_reach:            #判断是否能够当前节点i
                return False
    
            max_reach = max(max_reach,i+nums[i]) 

            if max_reach >= len(nums-1):
                return True
            
        return False
            