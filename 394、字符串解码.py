"""
用两个栈，一个用来存储数字，一个用来存储字符串,遇见一个[,将数字和字符串压入栈中，当遇见一个] 则拿出来一个数字和字符串准备

"""
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        current_num = 0
        current_str = ''   ##这里的currenrt_str维护了两个功能，第一个功能：将所有的[ 后的str记录压入栈中，  第二个功能：因为所有的]都在左括号后面，所以出现第一个右括号时，就开始解析函数了。


        for char in s:
            if char.isdigit():
                current_num = current_num*10+int(char)
            elif char == '[':
                stack.append((current_num,current_str))
                current_num = 0
                current_str = ''
            elif char == ']':
                decode_num,decode_str = stack.pop()
                current_str = decode_str+current_str*decode_num
            else:
                current_str += char
            
        return current_str
    

