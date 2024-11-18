###递归法，但是如果目标函数n特别大，就会超时 比如n =38  那结果就是63245986

#递归法
# class Solution(object):
#     def climbStairs(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         # 记录结果的列表，便于递归过程中更新
#         result = [0]
        
#         def hs(sum, n):
#             # 如果当前和等于目标n，说明找到了一种有效的方案
#             if sum == n:
#                 result[0] += 1  # 更新结果
#                 return
#             # 如果当前和超过目标n，说明这条路径不合法，返回
#             if sum > n:
#                 return
            
#             # 遍历每步可以爬的台阶数
#             for step in [1, 2]:
#                 hs(sum + step, n)
        
#         hs(0, n)  # 从第0阶开始爬楼
#         return result[0]  # 返回最终结果

# tem = Solution()
# print(tem.climbStairs(38))  # 输出：13


#动态规划算法    直接有个公式，第n个楼梯的爬法等于n-1次和n-2次的爬法

class Solution(object):
    def climbStairs(self, n):
        dp =[0]*(n+1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        for i in range(3,n+1):
            dp[i] = dp[i-1]+dp[i-2]

        return dp[n]