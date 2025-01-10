"""
这代码也是妙的很、     进一步加深对位运算的了解。
"""
class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i >> 1] + (i & 1)  # 右移一位并加上最低位是否为 1
        return dp
        