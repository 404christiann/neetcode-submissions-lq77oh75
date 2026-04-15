# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # we need to create a dummy node. 
        # we call it tail
        # we will iterate through until l1 & l2 are not None. 
        # in each iteration we check if l1 < l2. 
        # if they are then we point our tail.next to l1.
        # after that we need to move to the next node in l1. so l1 = l1.next 
        # (in the else case we do the same thing)

        l1 = list1 
        l2 = list2
        dummy = ListNode()
        tail = dummy
        while l1 and l2:
            if l1.val<l2.val:
                tail.next = l1
                # update the l1 pointer. 
                l1 = l1.next                
            else:
                tail.next = l2
                l2 = l2.next
            # update the pointer for the tail linked list. 
            tail = tail.next 

        # when one list finally runs out, we point the rest of the list to the remaining.
        # since its sorted it works out. 
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2
        return dummy.next
        





            



                









        
        