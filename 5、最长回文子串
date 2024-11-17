
##中心扩展法

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def help(left,right):
            while left>=0 and right<len(s) and s[left]==s[right]:
                left -= 1
                right += 1
            return s[left+1:right]

        longent_str = ""
        for i in range(len(s)):
            single = help(i,i)
            double = help(i,i+1)
            if len(single) >= len(longent_str):
                longent_str = single
            elif len(double) >= len(longent_str):
                longent_str = double
        return longent_str       




tem = Solution()
print(tem.longestPalindrome(s="abcdad"))
