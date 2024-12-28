"""
对于动态规划问题，最重要的就是建立第n个与之前节点的关系
打家劫社，dp[i]表示偷到第i个房子时的金额，而dp[i]要么为dp[i-2]+nums[i] 要么就是还是dp[i-2]
"""
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        if len(nums)==1:
            return nums[0]

        tem_price1 = 0
        tem_proce2 = nums[0]

        price = [0]*len(nums)
        price[0] = 0
        price[1] = nums[0]
        for i in range(1,len(nums)):
            price[i] = max(tem_price1+nums[i],tem_proce2)
            tem_price1 = tem_proce2
            tem_proce2 = price[i]
        return max(price[-1],price[-2])



tp = Solution()
print(tp.rob([1,3,6,7,9]))        
