class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        ### Thought process
        - Basic sliding window concept 
        - We move `l` left if we notice a repeated letter `s[r]` untill the condition is no longer violated
        - If the repeated condition is not violated `l` is stationary marking the start of our substring and we grow the sliding window from the right side with `r` 
        - Two key things to know here are : sliding window approach with left and right pointers sliding across our array, character map 
        
        ### Notes 
        - time complexity : $O(n)$
        - space complexity : $O(n)$ because of `subs` hashset 
        """
        subs = set()
        l = 0
        res = 0
        
        for r in range(len(s)):
            while s[r] in subs:
                subs.remove(s[l])
                l += 1
            
            subs.add(s[r])
            res = max(res, r - l + 1)

        return res


