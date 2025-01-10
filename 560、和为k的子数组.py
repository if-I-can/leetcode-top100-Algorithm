"""
理论上我的方法也行，可是超出时间限制了。
"""

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        
        for i in range(len(nums)):
            current_sum = 0  # 当前子数组的和
            for j in range(i, len(nums)):
                current_sum += nums[j]  # 更新子数组的和
                if current_sum == k:  # 如果和等于k，增加计数
                    count += 1
        
        return count


"""
高级算法
"""
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        prefix_sum = 0
        prefix_map = {0: 1}  # 初始化前缀和为 0 的情况，表示从数组开头到当前元素的和为 0 的情况
        
        for num in nums:
            prefix_sum += num  # 计算当前前缀和
            
            # 如果 (prefix_sum - k) 已经出现过，表示存在一个子数组和为 k
            if prefix_sum - k in prefix_map:
                count += prefix_map[prefix_sum - k]  # 累加出现的次数
            
            # 更新哈希表，记录当前前缀和出现的次数
            if prefix_sum in prefix_map:
                prefix_map[prefix_sum] += 1
            else:
                prefix_map[prefix_sum] = 1
        
        return count
