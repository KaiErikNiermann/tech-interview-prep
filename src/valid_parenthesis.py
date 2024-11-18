class Solution:
    def isValid(self, s: str) -> bool:
        """
        ### Thought process 
        - I think a good way to think about this is the False and Passing condition 
        - False condition : false condition without corresponding opening bracket 
        - Passing condition : stack is empty, signifying that all brackets have been closed
        - We can use a dictionary to map the closing brackets to the opening brackets
        
        ### Notes
        - time complexity is $O(n)$
        - space complexity is $O(n)$ 
        """
        c_map = {')' : '(', '}' : '{', ']' : '['}
        c_stack = []

        for c in s: 
            if c not in c_map: 
                c_stack.append(c)
                continue
            if not c_stack or c_stack[-1] != c_map[c]:
                return False
            c_stack.pop()

        return not c_stack
    