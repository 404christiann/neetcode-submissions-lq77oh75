# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # need to account for the empty list case. 
        slowPointer = head
        fastPointer = head
        # Ensure fast and the node it's jumping to are not None 
        while fastPointer and fastPointer.next:
            # if there is a cycle the faster pointer will eventually 
            # hit the slow pointer 
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next
            if slowPointer == fastPointer:
                return True    
        return False
        