"""
这题我觉的有难度的，要弄懂3个状态：第i天是卖出时的利润，是冷冻期的利润，持有的时候的利润(继续持有的时候，或者是买入的时候也算是持有)
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        sell = [0]*len(prices)
        hold = [0]*len(prices)
        cooltime = [0]*len(prices)
        hold[0] = -prices[0]



        for i in range(1,len(prices)):
            sell[i] = hold[i-1] + prices[i]
            hold[i] = max(hold[i-1],cooltime[i-1] - prices[i])
            cooltime[i] = max(cooltime[i-1],sell[i-1])



        return max(max(cooltime),max(sell))

        