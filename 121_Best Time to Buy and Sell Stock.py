class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        acc = []
        for i in range(len(prices) -1):
            j = max(prices[i+1:])
            if j > prices[i]:
                acc.append(j-prices[i])
        
        if acc == []:
            return 0
        return max(acc)