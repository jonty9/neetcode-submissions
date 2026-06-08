class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 0
        p = 0

        for i in range(len(prices)):
            if prices[i] < prices[buy]:
                buy = i
                if sell < buy:
                    sell = buy
            elif prices[i] > prices[sell]:
                sell = i
            
            
            newProf = prices[sell] - prices[buy]
            if newProf > p:
                p = newProf

        return p
