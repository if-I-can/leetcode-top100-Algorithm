
##双指针 从两遍往中间走

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left,right= 0,len(height)-1
        max_water = 0
        while left != right:
            width = right-left
            min_length = min(height[left],height[right])
            max_water = max(max_water,width*min_length)
            if height[left] > height[right]:
                right -= 1
            else:
                left+=1
        return max_water



tem = Solution()
print(tem.longestPalindrome(s="abcdad"))
