##  和之前的递归的区别就是，这个没有限制条件，所以在hs 函数开头 不用加入跳出的条件，然后这里是不重复元素，所以递归的时候，是从下一个元素开始，i+1 

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []

        def hs(start,current):
            result.append(list(current))

            for i in range(start,len(nums)):
                current.append(nums[i])
                hs(i+1,current)
                print(current)
                current.pop()

        hs(0,[])    #  我在想空集是怎么可能 被递归出来的，原来只要刚开始append就好了、
        return result

tep = Solution()
print(tep.subsets([1,2,3]))
