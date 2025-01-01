"""
Set 也是很常用的。  这里也学习一下for 和 if在一块的时候的语法。

"""

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        

        num = set(nums)
        
        result = [i for i in range(1,len(nums)+1) if i not in num]

        return result
        