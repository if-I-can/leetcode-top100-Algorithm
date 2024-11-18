class Solution():
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        def hs(index,sum,pailie):
            if sum == target:
                result.append(list(pailie))
                return
            elif sum > target:
                return
            
            for i in range(len(candidates)):
                pailie.append(candidates[i])
                hs(i,sum+candidates[i],pailie)
                pailie.pop()

        hs(0,0,[])
        return result
    

