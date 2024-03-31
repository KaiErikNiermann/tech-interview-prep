from typing import List
from collections import defaultdict
class Solution: 
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
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
        
        
        > Interestingly enough this algorithm actually runs slower than using `sorted` in python, I'm not sure why, `sorted` uses Timsort which has a best case TC of $\\Omega(n)$ and worst case of $O(n\\log n)$ so in theory it should at most be the same speed as this but apparently not, could be that there are other optimizations with `sorted` that I'm not aware of
        """
        res = defaultdict(list)
        
        for s in strs:
            count = [0] * 26 # 26 letters in the alphabet
            for c in s:
                count[ord(c) - ord('a')] += 1
                
            res[tuple(count)].append(s)
            
        return list(res.values())
        
    def groupAnagramsSorting(self, strs: List[str]) -> List[List[str]]:
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