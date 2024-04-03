class Solution:
    def maxArea(self, height: list[int]) -> int:
        """
        ### Thought process 
        - Once again basic two point setup so `l, r = 0, len(height) - 1` and `while l < r`
        - The area is the base length times $ r - l $ the height of the smaller wall $\\text{min}(h[l], h[r])$
        - We can move the pointer with the smaller wall since moving the pointer with the larger wall will only decrease the area
        - We repeat this process until the pointers cross over
        
        ### Notes
        - time complexity: $O(n)$ just a single loop 
        - space complexity: $O(1)$ 
        """
        l, r = 0, len(height) - 1
        max_area = 0
        
        while l < r:
            max_area = max(max_area, (r - l) * min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
                
        return max_area
    
    def maxAreaBruteForce(self, height: list[int]) -> int:
        """
        ### Thought process 
        - We can brute force this by checking all possible areas
        - We can do this by having two loops and checking all possible combinations of areas
        - We can then return the maximum area
        
        ### Notes
        - time complexity: $O(n^2)$ ⚠️ does not pass time limit
        - space complexity: $O(1)$
        """
        max_area = 0
        
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                max_area = max(max_area, (j - i) * min(height[i], height[j]))
                
        return max_area

print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))