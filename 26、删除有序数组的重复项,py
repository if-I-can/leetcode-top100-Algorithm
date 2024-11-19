class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ak = []
        for i in range(0,len(nums)):
            if nums[i] not in ak:
                ak.append(nums[i])
        print(ak)
        for i in range(len(ak)):
            nums[i] = ak[i]
        
        nums = nums[:len(ak)]
        return len(ak)
        
tep = Solution()
print(tep.removeDuplicates([1,1,2]))