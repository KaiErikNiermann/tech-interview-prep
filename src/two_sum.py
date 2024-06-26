class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        ### Thought process
        - We create a dictionary to store value -> index 
        - We recognize the property `a + b = target` -> `target - a = b` -> ans = [idx(target - a), idx(a)]
        - Since we now only need the current element and target, we can simply:
        - iterate through the list 
        - compute the difference 
        - see if the difference is in the dictionary
            
        ### Notes 
        - time complexity: O(n)
        - space complexity: O(n)
        
        """
        m = {}
        for idx, i in enumerate(nums):
            diff = target - i
            if diff in m: 
                return [m[diff], idx] 
            m[i] = idx
            