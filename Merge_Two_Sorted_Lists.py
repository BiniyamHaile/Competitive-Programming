# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1 =  list1
        head2 = list2
        returned  =  ListNode()
        pointer = returned
        while head1 and head2:
            if head1.val <= head2.val:
                pointer.next = ListNode(head1.val)
                head1 = head1.next
                
            else:
                pointer.next = ListNode(head2.val)
                head2 = head2.next
            pointer = pointer.next
            
        
        while head1:
            pointer.next = ListNode(head1.val)
            head1 = head1.next
            pointer = pointer.next
        while head2:
            pointer.next = ListNode(head2.val)
            head2 = head2.next
            pointer = pointer.next
        return returned.next
        


        
