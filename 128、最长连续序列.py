"""
这个题没啥难度，但时间复杂度只能是O(n)所以要保证每个for下面不能再有大量的运算。我刚开始是想着遍历所有元素然后while判断每一个为起点时的长度，取max
所以换一种思想，先确定当前遍历的元素是不是起点。
"""


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        nums_set = set(nums)
        result = 0

        for i in nums_set:
            if i-1 not in nums_set:
                current_num = i
                temp = 1 
                while current_num+1 in nums_set:
                    temp +=1
                    current_num += 1
                result = max(temp,result)

 
        return result

tp = Solution()
print(tp.longestConsecutive([1,2,3,4,8,11,12,13,14,15,16,17]))