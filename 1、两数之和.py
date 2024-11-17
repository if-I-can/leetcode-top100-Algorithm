# 给定一个整数数组
# nums
# 和一个整数目标值
# target，请你在该数组中找出
# 和为目标值
# target
# 的那
# 两个
# 整数，并返回它们的数组下标。
# 你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。
# 你可以按任意顺序返回答案。
# 示例
# 1：
# 输入：nums = [2, 7, 11, 15], target = 9
# 输出：[0, 1]
# 解释：因为
# nums[0] + nums[1] == 9 ，返回[0, 1] 。
# 示例
# 2：
# # 输入：nums = [3, 2, 4], target = 6
# 输出：[1, 2]
# 示例
# 3：
# 输入：nums = [3, 3], target = 6
# 输出：[0, 1]

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 创建一个字典来保存每个数字对应的索引
        num_to_index = {}

        for i, num in enumerate(nums):
            print(i,num)
            complement = target - num
            print(complement)
            # 检查补数是否已经在字典中
            if complement in num_to_index:
                return [num_to_index[complement], i]
            # 将当前数字和它的索引存入字典
            num_to_index[num] = i


# 示例调用
solution = Solution()
result = solution.twoSum([2, 7, 11, 15], 9)
print(result)  # 输出: [0, 1]
