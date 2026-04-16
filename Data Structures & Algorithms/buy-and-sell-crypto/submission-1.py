class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # eg. prices = [10,1,5,6,7,1]
        # output:6 buy at 1, sell at 7 profit = 7-1 = 6
        finalProfit = 0
        for i in range(len(prices)):
            j = len(prices) - 1 
            while i < j:
                currentProfit = prices[j] - prices[i]
                if currentProfit > finalProfit:
                    finalProfit = currentProfit
                j-=1
        print(finalProfit)
        return finalProfit
                

        