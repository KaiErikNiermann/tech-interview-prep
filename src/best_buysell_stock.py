class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        ### Thought process
        - The main idea is just that the find the maximum profit we just store the lowest price and compare this to all the other values 
        
        ### Notes 
        - time complexity : $O(n)$
        - space complexity: $O(1)$
        """
        res = 0 
        
        lowest = prices[0]
        for p in prices: 
            if p < lowest:
                lowest = p
            res = max(res, p - lowest)
        return res