"""
这题挺难的，理解逻辑

"""
from collections import Counter
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        need = Counter(t) ## 目标元素 的每个元素的数量
        window = Counter() ## 初始化定义一个空的字典，记录移动窗口中每个元素的数量
        
        left,right = 0,0 #  初始化窗口从0开始
        start,min_len = 0,float('inf')

        valid = 0
        while right < len(s):

            window[s[right]] += 1

            if s[right] in t and window[s[right]] == need[s[right]]:
                valid += 1

            while valid == len(need) and left <= right:
                if right - left + 1 < min_len:
                    start = left
                    min_len = right - left +1

                window[s[left]] -= 1                             ## 这里还是要好好理解一下的。
                if s[left] in need and window[s[left]] < need[s[left]]:
                    valid -= 1
                left += 1

            right += 1


        return '' if min_len == float('inf') else s[start:start+min_len]

tp = Solution()

print(tp.minWindow(s = "ADOBECODEBANC", t = "ABC"))
        