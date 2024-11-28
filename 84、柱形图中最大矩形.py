##非常好的  栈 题，主要是理解计算面积时的宽度，可以把索引理解为右边界，每次清算时，清算的是当前pop的柱子的右边，确保递增，这也是为什么最后要
###一个0，这样才能把所有的元素pop出栈。
#  单调栈

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []  # 栈，用来存储柱子的索引
        max_area = 0  # 最大矩形面积
        heights.append(0)  # 在末尾添加一个高度为0的柱子，确保所有柱子出栈

        for i in range(len(heights)):
            # 如果当前柱高小于栈顶柱高，计算矩形面积
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]  # 栈顶柱高
                # 宽度：如果栈为空，说明宽度为当前索引，否则为索引差
                w = i if not stack else i - stack[-1] - 1
                print(w)
                max_area = max(max_area, h * w)
            stack.append(i)  # 当前柱子的索引入栈

        return "al"

tep = Solution()
print(tep.largestRectangleArea([1,3,5]))








        