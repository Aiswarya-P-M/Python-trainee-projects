class Buyandsell:
    def maxProfit(self,prices):
            total_profit =0
            for i in range(0,len(prices)-1):
                if prices[i+1]>prices[i]:
                    total_profit += prices[i+1]-prices[i]
            return total_profit
prices=[7,1,5,3,6,4]
maxp=Buyandsell()
print("Total profit is:",maxp.maxProfit(prices))
