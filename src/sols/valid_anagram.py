from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        ### The basic thought process is the following
        - Triviall if the words have a different length we return False 
        - We create two dictionaries to store the frequency of each character in the words
        - We compare the dictionaries to see if they are equal
        
        ### Notes 
        - time complexity: O(n)
        - space complexity: O(n)
        
        """
        if len(s) != len(t):
            return False
        
        s_dict = {}
        t_dict = {}
        
        for i in range(len(s)):
            s_dict[s[i]] = s_dict.get(s[i], 0) + 1
            t_dict[t[i]] = t_dict.get(t[i], 0) + 1
            
        return s_dict == t_dict
    
    def isAnagramSort(self, s: str, t: str) -> bool:
        """
        ### The basic thought process is the following
        - Triviall if the words have a different length we return False 
        - We sort the words and compare them
        
        ### Notes 
        - time complexity: O(n^2) -> O(nlogn) 
        - space complexity: O(n) -> O(1)
        
        """
        if len(s) != len(t):
            return False
        
        return sorted(s) == sorted(t)
    
    def isAnagramCounter(self, s: str, t: str) -> bool:
        """
        A bit of a cheat, but we can use the Counter class from the collections module
        """
        return Counter(s) == Counter(t)