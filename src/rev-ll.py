from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val) + " -> " + str(self.next)

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        ### Thought process 
        - Broad idea is that we iterative through the list, and place the previous into the next position 
        - To explain the 4 lines of code in the loop 
        - We first store the next position, since we need to go to this, but we will also modify the pointer to this 
        - We then modify the point, essentially directing the arrow in the other direction
        - We store this in `prev` to use in the next iteration 
        - We go to the next iteration
        
        ### Notes 
        - time complexity : $O(n)$
        - space complexity : $O(1)$
        """
        prev, curr = None, head
        
        while curr: 
            tmp = curr.next 
            
            # setting point and saving previous
            curr.next = prev 
            prev = curr 
            
            curr = tmp
            
        return prev
    
print(Solution().reverseList(ListNode(1, ListNode(2))))
print(Solution().reverseList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))) # 5 -> 4 -> 3 -> 2 -> 1