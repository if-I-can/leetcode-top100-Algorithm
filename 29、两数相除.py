class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        if divisor == 0:
            return ("Divisor cannot be zero")
        if dividend == 0:
            return 0  # If dividend is zero, the result is zero
        
        # Handle the overflow case: INT_MIN divided by -1
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        
        # Determine the sign of the result
        fuhao = (dividend > 0) != (divisor > 0)
        
        # Take absolute values for easier handling
        dividend, divisor = abs(dividend), abs(divisor)
        result = 0

        # Perform division using bit shifting (doubling divisor)
        while dividend >= divisor:
            temp, multiple = divisor, 1
            while dividend >= (temp << 1):  # Doubling the divisor
                temp <<= 1
                multiple <<= 1
            dividend -= temp
            result += multiple

        # Apply the sign to the result
        if fuhao:
            result = -result

        # Return the result, ensuring it's within the 32-bit integer range
        return min(max(result, INT_MIN), INT_MAX)