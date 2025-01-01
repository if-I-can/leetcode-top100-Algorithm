"""
做了很多动态规划了，我要总结一下了。


这个题就是逻辑我懂了，一下子就做出来了。
"""


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        
        dp = [1]*len(nums)

        for i in range(len(nums)):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i] = max(dp[i],dp[j]+1)

        return max(dp)
        