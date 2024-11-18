"""
Kadane算法查找一个连续子数组，且要确保其和最大，思想为:  max_sum加上current_element时，若比原来的max_sum大，则将其加到现有列表，否则从当前元素重新开始计算
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = nums[0]
        current_sum = nums[0]
        for i in range(1,len(nums)):
            current_sum = max(nums[i],current_sum+nums[i])
            max_sum = max(max_sum,current_sum)
        return max_sum
    
