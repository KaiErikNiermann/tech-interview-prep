class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        ### Thought process 
        - Problem uses some of the usual things, frequency map to store substring `t` and the window of `s`
        - Key observation, to achieve an $O(n)$ solutions we observe that we can define the condition of a substring being contained within a window as a single variable `have` being compared to `need`, where both variables are numeric counts representing the specific letters of the substring 
        - We keep track of the window size and window start and end indices
        - Abstractly the problem uses the general sliding window approach, so the `r` pointer iterates through the loop as normal and the `l` pointer iterates on a condition 
        - During the iteration we consider 3 main conditions : `have != need` $\\rightarrow$ expand window , `window[c] == subs[c]` $\\rightarrow$ increment `have`, `while have == need` $\\rightarrow$ move the `l` pointer and check if we found a new smallest substring
         
        ### Notes 
        - time complexity : $O(n)$
        - space complexity : $O(n)$
        """
        if t == "": return ""

        subs, window = {}, {}
        for c in t:
            subs[c] = 1 + subs.get(c, 0)

        have, need = 0, len(subs)
        res, res_l = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in subs and window[c] == subs[c]:
                have += 1

            while have == need:
                # update our result
                if (r - l + 1) < res_l:
                    res = [l, r]
                    res_l = r - l + 1
                    
                # pop from the left of our window
                window[s[l]] -= 1
                if s[l] in subs and window[s[l]] < subs[s[l]]:
                    have -= 1
                l += 1
                
        l, r = res
        return s[l : r + 1] if res_l != float("infinity") else ""
