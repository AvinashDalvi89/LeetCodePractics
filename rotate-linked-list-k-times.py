# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None : return head 
        last = curr = head
        size = 1
        while last.next:
            last = last.next
            size += 1
        last.next = head
        k = k % size
        for i in range(0, size-k):
            last = last.next
        curr = last.next
        last.next = None
        return curr
            
