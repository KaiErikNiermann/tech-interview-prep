from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        """
        ### Thought process
        - Use `set()` for O(1) lookups of neighbors
        - Logic is: if `n` has no Left neighbor `=>` start of sequence otherwise keep incrementing
        - If start of sequence found then keep incrementing till no Right neighbor found
        - Keep track of longest sequence found
        - Basic idea is just to find max length of sequence by recognizing start (n - 1 not in set) and end (n + length (+1) not in set)
        
        ### Notes 
        - time complexity : $O(n)$ 
        - space complexity : $O(n)$
        """
        nums_set = set(nums)
        longest = 0 
        
        for n in nums:
            # no left neighbor => start of seq
            if (n - 1) not in nums_set: 
                
                # find the length of the sequence
                length = 0
                while (n + length) in nums_set: 
                    length += 1
                longest = max(longest, length)
                
        return longest