class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return intervals

        intervals.sort(key = lambda x: x[0])

        merged = [intervals[0]]

        for i in range(1,len(intervals)):
            current = intervals[i]
            if current[0] <= merged[-1][1]:
                if current[1] <= merged[-1][1]:
                    merged[-1] = merged[-1]
                else:
                    merged[-1] = [merged[-1][0],current[1]] 
            else:
                merged.append(current)

        return merged
    
tep = Solution()
print(tep.merge([[1,3],[2,4],[6,9]]))