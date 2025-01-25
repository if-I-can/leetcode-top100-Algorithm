"""
用双指针的方法来做，从两边往中间走，根据当前的max 值来确定是根据左指针来确定水量还是根据右指针来确定水量，
每移动一次的水量=当前方向的max-heiht[当前指针]

"""
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        
        left,right = 0,len(height)-1
        left_max,right_max = height[left],height[right]
        water = 0

        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max,height[left])
                water += max(0,left_max - height[left])
            else:
                right -= 1
                right_max = max(right_max,height[right])
                water += max(0,right_max-height[right])

        return water
