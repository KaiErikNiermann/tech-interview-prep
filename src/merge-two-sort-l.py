from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val) + " -> " + str(self.next)
    
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        ### Thought process 
        - there are 3 key ideas, the progression condition, so there being nodes still in either lists, the comparison condition, so for each pair getting the smaller node and progressing the pointer at the list, the tail condition where we attach the remainder of either list to the end
        - We create an empty LL to represent our combined list 
        - Then we iterate throughts the lists ensuring there is always something we can compare
        - if `l1.val < l2.val` we progress l1 to the next position 
        - if `l2.val < l1.val`we progress l2 to the next position 
        - in both cases we save the next node as whichever LL is smaller 
        - we then jump to the next position in our created LL
        - in the end we attach the remaining tail to the node 
        - since we want to return the start of the list we return the dummy node
        
        ### Notes 
        - time complexity : $O(n)$
        - space complexity : $O(n)$
        """
        dummy = node = ListNode()
        
        # stop condition
        while list1 and list2: 
            
            # comparison condition
            if list1.val < list2.val: 
                node.next = list1
                list1 = list1.next 
            else: 
                node.next = list2 
                list2 = list2.next 
                
            node = node.next 
            
        # tail condition
        node.next = list1 or list2 
        return dummy.next
    
    def mergeTwoSortedRecursive(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]: 
        """
        ### Thought process 
        - Same idea as above, if either list has reached the end we return the remained of the other 
        - For the comparison we progress (do `lo.next`) the list with the smaller value at the current position        
        """
        # stop + tail condition (base case)
        if not list1: return list2
        if not list2: return list2
        
        # comparison condition
        lo, hi = (list1, list2) if list1.val < list2.val else (list2, list1)
        lo.next = self.mergeTwoLists(lo.next, hi)