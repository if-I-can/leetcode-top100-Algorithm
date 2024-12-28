"""
要求时间复杂度O(n)  所以只能用一次循环
"""

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums_sorted = sorted(nums,reverse = True)
        return nums_sorted[k-1]
        