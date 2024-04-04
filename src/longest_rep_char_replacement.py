class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        ### Thought process 
        - Again a siliding window problem
        - The idea here is that our target substring consists of two components 
            
            1. The most frequent character
            
            2. The rest of the $k$ other characters (which we can flip to the most frequent character)
        
        - So we keep track of the most frequent character through a basic frequency map 
        - Now a trick we can do is we can break the letters in two types 
        
        a. belongs to the subword 
        b. does not belong to the subword             

        - Clearly if we can just deliniate ( separate ) the two, we can easily find the length of the subword by doing `all letters - violating letters`      
        - So we can define our `l` pointer as the point which separates the two types of characters, in the most simple sense all `l` is, is a counter of the violating characters, that is, everytime we have the violating condition `r - l + 1 - maxf > k` we increment `l` by 1, and decrement the frequency of the character at `l` by 1
        - The violating condition `r - l + 1 - maxf > k` is just a way of saying that the rest of the characters in our substring exceed the number of characters we can flip
        
        ### Notes
        - time complexity is $O(n)$
        - space complexity is $O(1)$
        """
        count = {}
        
        l = 0 
        maxf = 0 
        
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            maxf = max(maxf, count[s[r]])
            
            if r - l + 1 - maxf > k:
                print(r, l, maxf, count, s[l], s[r])
                count[s[l]] -= 1
                l += 1
                
        return len(s) - l # (r - l + 1) - (r - l + 1 - maxf) = maxf