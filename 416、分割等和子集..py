class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if sum(nums) % 2 != 0:
            return False

        mid = sum(nums)//2

        dp = [False]*(mid+1)
        dp[0] = True

        for num in nums:
            for i in range(mid,num-1,-1):
                dp[i] = dp[i] or dp[i-num]
        
        return dp[mid]
        
        
tp = Solution()
print(tp.canPartition([1,3,2,4,5]))