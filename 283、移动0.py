"""
如果            if nums[right] != 0:  则是0放到最后面， 如果是==0，则0其实是放在了最前面
"""
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left = len(nums)
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[right],nums[left] = nums[left],nums[right]
                left -= 1
