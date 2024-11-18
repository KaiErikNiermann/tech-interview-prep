import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        ### Thought process 
        - Not too much to think about here, just have to remmber that python has built in libs to check things (alot of languages generally have ".is" member functions)
        - Also good to remember string slice notation [start : stop : step] where [::-1] is a common way to reverse a string

        ### Notes 
        - time complexity : $O(n)$ 
        - space complexity : $O(n)$
        > If the interviewer asks for a space complexity of $O(1)$, we can use two pointers to iterate through the string, but if this is in an OA with no constraints, this is fine      
        """
        new = ""
        for i in s:
            if i.isalnum():
                new += i.lower()

        return new == new[::-1]
    
    def isPalindromeCompact(self, s: str) -> bool:
        """
        ### Thought process
        - We can also use rejex along with `.lower()` `[^a-zA-Z0-9 -]` removes everything non-alphanumeric
        - Same approach with comparison
        """
        s = re.sub(r'[^a-zA-Z0-9 -]', '', s.lower())
        return s == s[::-1]
    
    def isPalindromeFunctional(self, s: str) -> bool: 
        """
        ### Thought process 
        - Essentially this is a more functional way to of the original approach 
        - We can use `filter` to filter out the alphanumeric characters on the lowered string
        - Then we compare the **arrays** of the filtered string and the reversed filtered string
        """
        s: list[str] = list(filter(str.isalnum, s.lower()))
        print(s, s[::-1])
        return s == s[::-1]
        
    def isPalindromeTwoPoint(self, s: str) -> bool:
        """
        ### Thought process
        - If we want to avoid using extra space, we can use two pointers
        - We can use a lambda function to check if a character is alphanumeric
        - We can then iterate through the string with two pointers
        - If the character is not alphanumeric, we move the pointer
        - If the characters are not the same, we return False
        - If we reach the end, we return True
        
        ### Notes
        - time complexity: $O(n)$
        - space complexity: $O(1)$
        """

        isalphnum = lambda x: x.isalnum()

        left, right = 0, len(s) - 1
        
        while left < right:
            # avoid non alnum 
            while left < right and not isalphnum(s[left]):
                left += 1
            while left < right and not isalphnum(s[right]):
                right -= 1
            
            # char comparisn
            if s[left].lower() != s[right].lower():
                return False
            
            # char movement
            left += 1
            right -= 1
        
        return True