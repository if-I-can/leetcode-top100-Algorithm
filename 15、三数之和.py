class Solution(object):
    def threeSum(self, nums):

        length = len(nums)
        record = set()  # 使用集合自动去重
        for i in range(length):
            for j in range(i + 1, length):
                for k in range(j + 1, length):
                    triplet = sorted([nums[i], nums[j], nums[k]])  # 对三元组排序
                    if sum(triplet) == 0:
                        record.add(tuple(triplet))  # 将三元组添加到集合中
        return list(record)  # 将集合转换为列表输出

# 测试代码
target = Solution()
print(target.threeSum(nums=[-1, 0, 1, 2, -1, -4]))
