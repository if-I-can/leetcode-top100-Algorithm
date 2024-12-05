class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 创建一个长度为 n+1 的数组 dp，dp[i] 表示有 i 个节点的二叉搜索树的数量
        dp = [0] * (n + 1)
        
        # 空树和只有一个节点的树都有 1 种可能
        dp[0] = 1
        dp[1] = 1
        
        # 从 2 到 n 逐步计算每个 dp[i]
        for i in range(2, n + 1):
            # 对于每个 i，计算它的二叉搜索树种数
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]
        
        # 返回 dp[n] 即为答案
        return dp[n]
