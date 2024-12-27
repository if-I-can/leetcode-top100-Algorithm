class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_subarray = max_subarray = result = nums[0]

        for num in nums[1:]:
            if num < 0:
                min_subarray,max_subarray = max_subarray,min_subarray


            min_subarray = min(num,num*min_subarray)
            max_subarray = max(num,num*max_subarray)

            result = max(result,max_subarray)
        return result



tp = Solution()
print(tp.maxProduct([3,2,4,-1,2,4]))