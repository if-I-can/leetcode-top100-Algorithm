class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []

        def backtrack(current, remaining):
            # 当当前排列的长度等于初始数组的长度时，保存当前排列
            if not remaining:
                result.append(current[:])  # 保存current的拷贝
                return
            
            for i in range(len(remaining)):
                # 选择当前元素加入current
                current.append(remaining[i])
                
                # 剩余未使用的数字
                next_remaining = remaining[:i] + remaining[i+1:]
                print(next_remaining)
                # 递归
                backtrack(current, next_remaining)
                
                # 回溯
                current.pop()

        backtrack([], nums)  # 初始状态
        return result


# 测试代码
tep = Solution()
print(tep.permute([1, 2, 3]))
