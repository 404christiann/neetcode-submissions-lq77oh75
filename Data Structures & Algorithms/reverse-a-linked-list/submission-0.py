# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr:
            nxt = curr.next    # Save the 'future' (eventually becomes None)
            curr.next = prev   # Flip! (On loop 1, this points to None)
            
            # The Label Hand-off
            prev = curr        # prev moves to the node we just finished
            curr = nxt         # curr moves to the node we saved
            
        return prev            # prev is now the new head!
            
