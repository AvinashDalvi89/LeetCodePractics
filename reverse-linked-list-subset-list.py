# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if not head:
            return None
        curr, prev = head, None
        while left > 1:
            prev = curr
            curr = curr.next 
            left,right = left-1, right-1 
        tail, con = curr, prev
        while right:
            third = curr.next
            curr.next = prev
            prev = curr
            curr = third 
            right -= 1
        if con:
            con.next = prev
        else:
            head = prev
        tail.next = curr
        return head
