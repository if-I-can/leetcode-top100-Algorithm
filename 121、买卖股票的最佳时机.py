class Solution(object):           #这是我自己最开始的暴力解法，理论没有问题，但是复杂度是O(n²)，卡在了时间上
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        result = []
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if prices[i]>prices[j]:
                    continue
                else:
                    result.append(prices[j]-prices[i])
        if not result:
            return 0
        else:
            return max(result)
    
tep = Solution()
print(tep.maxProfit(prices=[7,6,4,3,1]))

"""优化后：贪心算法:维护最小买入价格并实时更新最大利润"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = float('inf')  # 初始化为无穷大，表示初始没有买入
        max_profit = 0  # 初始化最大利润为0

        for price in prices:     #因为本身卖出日期不可能在卖入日期之前，我那种确实想复杂了
            # 更新最低买入价格
            min_price = min(min_price, price)
            # 计算当前卖出利润
            profit = price - min_price
            # 更新最大利润
            max_profit = max(max_profit, profit)

        return max_profit
