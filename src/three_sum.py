from collections import defaultdict

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """
        ### Thought process
        - Broad idea: We sort our array, then take a value `a` and consider the values to the `l` and `r`. Since the array is sorted moving `r` closer to `l` will decrease the sum and moving `l` closer to `r` will increase the sum. 
        - We can skip positive integers, since it is impossible to sum to 0 (e.g. [1, 2, 3])
        - We can skip duplicates to avoid duplicates in our result 
        - Basic two pointer setup so 1. init pointers 2. loop while they havent crossed over
        - Check the 3 cases of the sum being too large, too small, or just right
        - If the sum is just right then append the result, move the pointers and skip duplicates
        
        ### Notes
        - time complexity: $O(n\\log n + n^2)$ -> $O(n^2)$
        - space complexity: $O(1)$ / $O(n)$ depending on the implementation of sort
        """
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            
            # Skip positive integers, impossible to sum to 0
            if a > 0:
                break

            # Skip duplicates
            if i > 0 and a == nums[i - 1]:
                continue

            # Init two pointers
            l, r = i + 1, len(nums) - 1
            
            while l < r:
                threeSum = a + nums[l] + nums[r]
                # If the sum is too large, we need to decrease the sum
                if threeSum > 0:   
                    r -= 1
                
                # If the sum is too small, we need to increase the sum
                elif threeSum < 0: 
                    l += 1
                    
                # If the sum is 0, we append the result
                else:             
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    
                    # Skip duplicates
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                        
        return res
                

print(Solution().threeSum([-1,0,1,2,-1,-4]))
print(Solution().threeSum([0, 0, 0]))
                
                