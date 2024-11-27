### 这个题还是有点难度的，两个循环+双指针，需要控制变量

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,n-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                left = j+1
                right = len(nums)-1
                while left<right:
                    total = nums[i]+nums[j]+nums[left]+nums[right]
                    if total == target:
                        result.append([nums[i],nums[j],nums[left],nums[right]])

                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        while left < right and nums[right] == nums[right-1]:
                            right += 1
                        left += 1
                        right -= 1
                    elif total< target:
                        left += 1
                    else:
                        right -= 1
                
        return result
    