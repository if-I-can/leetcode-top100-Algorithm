# #有效的括号
# """
# 方法一
# """
# class Solution(object):
#     def isValid(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         number1 = s.count('(')
#         number2 = s.count('[')
#         number3 = s.count('{')
#         number1_1 = s.count(')')
#         number2_2 = s.count(']')
#         number3_3 = s.count('}')
#         if number1 == number1_1 and number2 == number2_2 and number3 == number3_3:
#             return True
#         else:
#             return False
#
#
#
# initial = Solution()
# result = initial.isValid(s='[])')
# print(result)
"""
方法二
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        while '()' in s or '[]' in s or '{}' in s:
            s = s.replace('()','')
            s = s.replace('[]','')
            s = s.replace('{}','')

            return s == ''


initial = Solution()
result = initial.isValid(s='()')
print(result)