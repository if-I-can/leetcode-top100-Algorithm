##回朔算法+递归算法
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        final = []
        dict_number = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}

        if not digits:
            return []
        
        #回溯函数
        def huishuo(index,current_str):

            ## 退出递归的条件
            if index == len(digits):
                final.append(current_str)
                return
            
            #每次递归遍历每一个数字对应的字符串
            str_current = digits[index]
            for i in dict_number[str_current]:
                huishuo(index+1,current_str+i)

        huishuo(0,'')
        return final


tem = Solution()
print(tem.letterCombinations('23'))