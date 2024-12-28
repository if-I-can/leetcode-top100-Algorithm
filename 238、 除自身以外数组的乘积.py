class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answear = [1]*len(nums)

        prefix = 1
        for i in range(len(nums)):
            answear[i] = prefix
            prefix *= nums[i]
        
        suffix = 1
        for i in range(len(nums)-1,-1,-1):
            answear[i] *= suffix
            suffix *= nums[i]

        return answear

        