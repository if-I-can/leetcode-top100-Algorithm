class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0])

        height = [0 for _ in range(n)]

        max_area = 0

        for i in range(m):
            for j in range(n):
                height[j] = height[j]+1 if matrix[i][j] =='1' else 0

            max_area = max(max_area, self.max_aver_row(height))

        return max_area
    
    def max_aver_row(self,height):
        max_area = 0
        stack = []
        height.append(0)

        for i in range(len(height)):
            while stack and height[i] < height[stack[-1]]:
                h = height[stack.pop()]
                w = i if not stack else i - stack[-1] -1
                max_area = max(max_area,w*h)
            stack.append(i)
        
        return max_area
