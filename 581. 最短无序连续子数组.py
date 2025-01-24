"""
这个题目很好理解，但这里用的双指针要学习的点还是有用的：
1、先确定无序区间。
2、确定无序区间的最小值和最大值。
3、基于最小值确定左边界，基于最大值确定右边。 
4、返回的是r-l+1
5、边界条件要好好记一下
"""

class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        left = 0
        right = len(nums)-1

        while left<len(nums)-1 and nums[left]<nums[left+1]:
            left += 1

        if left == len(nums)-1:
            return 1
        
        while right > 0 and nums[right] > nums[right-1]:
            right -= 1

        min_num = min(nums[left:right+1])
        max_num = max(nums[left:right+1])

        while left > 0 and nums[left] > min_num:
            left -= 1

        while right < len(nums) and nums[right] < max_num:
            right += 1

        return right - left +1 
        