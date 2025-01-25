"""
两种思路：1 图结构，若存在环，则说明会出现冲突  (暂不考虑)
2 深度有限搜索，如果整在访问的节点再一次被访问，则会出现冲突。（先看这种方法）


这题难度还是很高的。 但我做起来感觉还是挺顺的，把逻辑捋顺
"""

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        graph = [[] for _ in range(numCourses)]
        
        for k,v in prerequisites:
            graph[k].append(v)

        visited = [0] * numCourses

        def dfs(course):
            if visited[course] == 1:
                return False
            if visited[course] == 2:
                return True
            
            visited[course] = 1
            for j in graph[course]:
                if not dfs(j):
                    return False
            visited[course] = 2

            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
            





tp = Solution()
print(tp.canFinish(2,[[1,0],[0,1]]))
        