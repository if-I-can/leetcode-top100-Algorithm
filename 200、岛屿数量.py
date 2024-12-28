"""
深度优先搜索DFS
"""

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def dfs(grid,i,j):
            print(i,j)
            if i < 0 or j < 0 or i > len(grid)-1 or j > len(grid[0])-1 or grid[i][j]=='0':
                return
            grid[i][j] = '0'
            dfs(grid,i+1,j)
            dfs(grid,i,j+1)
            dfs(grid,i-1,j)
            dfs(grid,i,j-1)

        num_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    grid[i][j] = '0'
                    num_islands += 1
                    dfs(grid,i,j)
                    
            
        return num_islands
    
tp = Solution()
print(tp.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))