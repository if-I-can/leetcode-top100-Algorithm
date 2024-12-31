##  这个公式得记一下。。  dp中用来保存每个平方数的最少平方数的组成，而dp[i] 可以转换为dp[i-j*j]+1,公式想通了，都很简单。

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [float('inf')]*(n+1)
        dp[0] = 0
        
        for i in range(1,len(dp)):
            j = 1
            while j**2 <= i:
                dp[i] = min(dp[i],dp[i-j**2]+1)
                j += 1
        
        return dp[n]