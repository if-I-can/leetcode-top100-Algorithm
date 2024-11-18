class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        num_0,num_1,num_2 = 0,0,0
        for i in range(len(nums)):
            if nums[i] == 0:
                num_0 += 1
            elif nums[i] == 1:
                num_1 += 1
            elif nums[i] == 2:
                num_2 += 1
        for i in range(num_0):
            nums[i]=0        
        for i in range(num_0,num_0+num_1):
            nums[i]=1 
        for i in range(num_0+num_1,num_0+num_1+num_2):
            nums[i]=2 

        return nums
    
tep = Solution()
print(tep.sortColors([1,2,1,2,0,1]))