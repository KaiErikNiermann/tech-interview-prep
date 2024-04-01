from collections import defaultdict
from functools import cache
class Solution: 
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        """
        ### Thought process 
        - `res` stores word frequency -> list of words
        - `defaultdict(list)` is a dict that initalizes to list, avoids edge case of key not in dict
        - We iterate through the words  
        - We create a count of the frequency of each character in the word
        - We convert the count to a tuple to make it hashable (potentially unecessary in other langs)
        - `ord(c) - ord('a')` maps the ascii value of the character to a number between 0-25, this gives us the index to store the count
        - `count[ord(c) - ord('a')] += 1` increments the count of the character
        
        ### Notes
        - time complexity: $O(m\\times n)$ where $m$ is the number of words and $n$ is average the length of the word
        - space complexity: $O(m)$
        
        > Interestingly enough, this solution in practice actually appears to be *slower* than the solution using `sorting()` honestly im not too sure why. One reason a friend of mine come up with is that for short words the complexity reduces to $O(n\\log n)$ though in testing it seems even with considerably large words sorting seems to be faster, additionally this seems to hold for some other languages. For python the algorithm used past 3.11 is [nearly optimal mergesort](https://www.wild-inter.net/publications/munro-wild-2018). If anyone knows why its seemingly faster than counting do tell.
        """
        res = defaultdict(list)
        
        for s in strs:
            count = [0] * 26 # 26 letters in the alphabet
            for c in s:
                count[ord(c) - ord('a')] += 1
                
            res[tuple(count)].append(s)
            
        return list(res.values())
        
    def groupAnagramsSorting(self, strs: list[str]) -> list[list[str]]:
        """
        ### Thought process 
        - Similarly for the basic anagram problem, if we sort the words we can group them together 
        - We can use a dictionary to store the sorted word -> list of words
        
        ### Notes 
        - time complexity: $O(m\\times n\\log n)$ where $m$ is the number of words and $n$ is average the length of the word
        - space complexity: $O(m)$
        """
        res = defaultdict(list)
        for word in strs:
            res[tuple(sorted(word))].append(word)
            
        return list(res.values())
    
    
    def groupAnagramsFast(self, strs: list[str]) -> list[list[str]]:
        """
        ### Thought process
        - We can cache the key creation function to avoid recomputing the key
        - Rest of the code is the same as before
        """
        @cache 
        def make_key(s):
            return tuple(sorted(s))
        
        res = defaultdict(list)
        for word in strs:
            res[make_key(word)].append(word)
            
        return list(res.values())