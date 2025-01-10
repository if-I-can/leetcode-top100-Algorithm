"""
这个题用动态规划来做，然后有点绕 要深入理解一下这个公式。
"""

class Solution(object):
    def findTargetSumWays(self,nums, target):
        total_sum = sum(nums)
                # 如果 (total_sum - target) 是奇数或小于 0，则无解
        if (total_sum - target) % 2 == 1 or total_sum < target:
            return 0

        subset_sum = (total_sum - target) // 2
        dp = [0] * (subset_sum + 1)
        dp[0] = 1

        for num in nums:
            for j in range(subset_sum, num - 1, -1):
                dp[j] += dp[j - num]

        return dp[subset_sum]
    




        

