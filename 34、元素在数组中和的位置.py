#完全是自己写的

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        if not nums:
           return [-1,-1]
        elif target not in nums:
            return [-1,-1]
        else:
            for i in range(len(nums)):
                if nums[i] == target:
                    result.append(i)
            return [result[0],result[-1]]
                    


tep = Solution()
print(tep.searchRange([1,2,3],3))