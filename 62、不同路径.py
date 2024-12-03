# m*n的矩阵，从左上角走到右下角的路径总和
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 1 and n == 1:
            return 1

        # 初始化路径矩阵
        d = [[0]*n for _ in range(m)]
        # 定义边界条件
        for i in range(1,m):
            d[i][0] = 1
        for j in range(1,n):
            d[0][j] = 1

        # 定义d[i][j]
        for i in range(1,m):
            for j in range(1,n):
                d[i][j] = d[i-1][j]+d[i][j-1]
        
        return d[m-1][n-1]


tep = Solution()
print(tep.uniquePaths(7,3))
