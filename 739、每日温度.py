"""
这个题的思想也要学习一下的，栈就是列表的索引[-1]的灵活应用

"""
    
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        answer = [0] * len(temperatures)
        stack = []  # 单调栈，用于存储索引

        for k, v in enumerate(temperatures):
            # 检查当前温度是否高于栈顶索引的温度
            while stack and v > temperatures[stack[-1]]:
                last_index = stack.pop()
                answer[last_index] = k - last_index
            stack.append(k)

        return answer



    
tp = Solution()
print(tp.dailyTemperatures([1,3,2,6]))