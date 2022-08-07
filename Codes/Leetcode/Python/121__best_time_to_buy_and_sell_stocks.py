class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_price = float(inf)
        max_price = float(-inf)
        for item in prices:
            min_price = min(item,min_price)
            max_price = max(max_price, item - min_price)
        return max_price