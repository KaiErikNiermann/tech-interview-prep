from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        ### Thought process
        - Create a set to store unique numbers 
        - Python `set()` has O(1) lookup 
        - If the number is already in the set, return True
        
        ### Notes 
        - time complexity: O(n)
        - space complexity: O(n)
        
        """
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False