class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left , right = 0 , len(nums)-1

        while left <= right:
            mid = (left + right)//2

            if nums[mid] == target:
                return mid
            
            if nums[left] <= nums[mid]:  # 位于左半球
                if nums[left] <= target < nums[mid]:
                    right = mid -1
                else:
                    left = mid +1
            else:
                if nums[mid] <= target <nums[right]: # 位于右序列
                    left = mid + 1
                else:
                    right = mid -1 

        return -1