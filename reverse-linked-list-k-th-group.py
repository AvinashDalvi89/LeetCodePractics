# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        def swapKnodes(dummy, head):
            for i in range(k-1):
                t = dummy.next
                dummy.next = head.next
                head.next = dummy.next.next
                dummy.next.next = t
            return head, head.next
        size = 0
        temp = head
        while temp:
            temp = temp.next
            size += 1
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        for i in range(size//k): #this wil return int value if output of size/k is decimal
            prev,head = swapKnodes(prev, head)
        return dummy.next
