from collections import defaultdict

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = defaultdict(list)
        for k,v in graph:
            graph(v).append(k)
        print(graph)






tp = Solution()
print(tp.canFinish(2,[[1,0],[0,1]]))
        