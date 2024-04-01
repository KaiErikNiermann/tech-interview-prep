class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        """
        ### Thought process
        - We do two passes to calculate all the pre and post products
        - Given an array $[a, b, c, d]$, the first pass is computed as $[1, (a), (ab), (abc)]$
        - The second pass is computed as $[(1)[bcd], (a)[cd], (ab)[d], (abc)]$
        - The result of these two passes gives us the answer
        - Its just doing the cumulative product forward then backward
        
        ### Notes 
        - time complexity: $O(n)$
        - space complexity: $O(n)$
        """
        res = [1] * len(nums)
        pre = 1
        
        # pre pass
        for i in range(len(nums)):
            res[i] = pre
            pre *= nums[i]
        post = 1
        
        # post pass
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= post
            post *= nums[i]
        return res