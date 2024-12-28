class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m,n = len(matrix),len(matrix[0])
        dp = [[0]*n for _ in range(m)]     #这个矩阵构造要记的熟一点，以后直接写，想都不要想

        max_squre = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    
                    if i == '0' or j =='0':
                        dp[i][j] = '1'
                    else:
                        dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1

                max_squre = max(max_squre,dp[i][j]**2)

        return max_squre
                
