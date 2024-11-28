class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tep = {}
        for i in range(len(nums)):
            if nums[i] not in tep.keys():
                tep[nums[i]] = 1
            else:
                tep[nums[i]] += 1
        
        result = [k for k,v in tep.items() if v == 1]
        return result[0]