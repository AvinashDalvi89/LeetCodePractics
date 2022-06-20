# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head.next == None:
            return None
        size = 0
        curr = head
        while (curr != None):
            curr = curr.next
            size += 1
        indexToSearch = size-n
        prev = head
        i=1
        if n == size:
            return head.next
        while (i<indexToSearch):
            prev = prev.next
            i +=1
        prev.next = prev.next.next
        return head
