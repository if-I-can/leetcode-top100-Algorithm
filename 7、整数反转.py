class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT_MIN,INT_MAX=-2**31,2**31
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        reverse = 0
        while x != 0:
            digit = x % 10
            x //= 10
            if reverse > INT_MAX//10 or (reverse == INT_MAX and digit>7):
                return 0
            reverse = reverse*10 +digit
        
        reverse = sign*reverse
        
        return reverse