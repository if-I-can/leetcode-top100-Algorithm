class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        tep = {}

        for i in nums:
            if i not in tep:
                tep[i] = 1
            else:
                tep[i] += 1

        print(tep.items())
        result = sorted(tep.items(), key=lambda x:x[1],reverse=True)
        print(result)
     
        return [i[0] for i in result[:k]]
    

tp = Solution()
print(tp.topKFrequent(nums=[2,2,2,1,2,3],k=2))