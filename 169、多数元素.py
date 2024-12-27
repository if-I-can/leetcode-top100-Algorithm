"""
熟练记一下这个 哈希表的get用法和迭代时的items用法
"""


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        for num in nums:
            count[num] = count.get(num,0) + 1
        
        for k,v in count.items:
            if v > len(nums)/2:
                return k


tp = Solution()
print(tp.majorityElement([3,2,3]))