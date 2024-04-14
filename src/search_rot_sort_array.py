from math import ceil

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """
        ### Thought process 
        - The key thing to remember here is that all this is, is a modified binary search 
        - All the modification `nums[l] <= nums[m]` does is ensure the condition required in binary search - that the target is in the interval of the split - continues to hold 
        - Again we determine the midpoint as `l + (r - l) // 2`
        - The different operations on the two pointers (same as for regular binary search) simply adjust the pointers to their correct positions in the segments ; that is, the `l` points to the leftmost index of the segment and `r` points to the rightmost index of the segment
        
        ### Notes 
        - time complexity is $O(log n)$
        - space complexity is $O(1)$
        """
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            
            if nums[l] <= nums[m]: 
                # left sorted segment
                if nums[l] <= target < nums[m]:
                    r = m - 1 
                else:
                    l = m + 1 
            else:
                # right sorted segment
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1       
