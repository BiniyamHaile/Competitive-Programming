# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        lista = []
        while head != None:
            lista.append(head.val)
            head = head.next
            
        
        if lista == lista[::-1]:
            return True
        else: 
            return False
                



        