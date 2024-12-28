##  这个公式得记一下。。  dp中用来保存每个平方数的最少平方数的组成，而dp[i] 可以转换为dp[i-j*j]+1

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        for i in range(101):