""""
这题很简单，也是查补一下

看来亦或符号^ 会自动将10进制按2进制进行计算。

"""

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        print(x)
        print(y)
        print(bin(x))
        print(bin(y))
        print(x^y)
        return bin(x^y).count('1')


tp = Solution()
print(tp.hammingDistance(4,6))