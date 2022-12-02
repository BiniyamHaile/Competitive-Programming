class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = head
        slow = head
        if slow != None:
            while (fast != None and fast.next != None):
                fast = fast.next.next
                slow = slow.next
                if (fast == None or fast.next == None):
                    return slow
        return slow
