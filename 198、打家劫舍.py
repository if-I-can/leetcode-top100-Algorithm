"""
对于动态规划问题，最重要的就是建立第n个与之前节点的关系
"""
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        if len(nums)==1:
            return nums[0]
        
        tep1 = 0
        tep2 = nums[1]
        result = 0
        price = [0,nums[1]]
        for i in range(2,len(nums)):
            price[i] = max(tep1,tep2+nums[i])
            tep1,tep2 = nums[i]+tep2,tep1
        return price[-1]

tp = Solution()
print(tp.rob([1,3,6,7,9]))        
