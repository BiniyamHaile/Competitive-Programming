# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        faster = head
        slower = head
        
        while faster.next and  faster.next.next  : 
            faster = faster.next.next
            slower = slower.next
            
            if not faster.next:
                print(slower)
                return slower
            
            if faster.next and not faster.next.next:
                
                return slower.next
            
         
        if slower.next:
            return slower.next
        return slower
           