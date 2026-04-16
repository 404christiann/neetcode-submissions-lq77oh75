class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # eg. prices = [10,1,5,6,7,1]
        # output:6 buy at 1, sell at 7 profit = 7-1 = 6
        # using sliding window technique. 
        left = 0 
        right = left+1
        maxProfit = 0

        while right <= len(prices) - 1:
            if prices[left] > prices[right]: 
                # increment both.
                left = right
                right += 1
            else:  
                totalProfit = prices[right] - prices[left]
                maxProfit = max(maxProfit, totalProfit)
                right += 1
        return maxProfit
            







        # This solution uses O(n^2) time. 
        # finalProfit = 0
        # for i in range(len(prices)):
        #     j = len(prices) - 1 
        #     while i < j:
        #         currentProfit = prices[j] - prices[i]
        #         if currentProfit > finalProfit:
        #             finalProfit = currentProfit
        #         j-=1
        # print(finalProfit)
        # return finalProfit
                

        