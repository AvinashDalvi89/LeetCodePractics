# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        # to divide list in middle using slow and fast ( turtle and hare concept) to keep pointer                 # at last node before middle and 
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        
        prev = slow.next = None # divide list in middle and point last of node before middle to None    
        # This will reverse left side of middle nodes
        while second:  
			sNext = second.next
			second.next = prev
			prev = second
			second = sNext
        first, second = head, prev
        while second:
            firstNext, secondNext = first.next, second.next
            first.next = second
            second.next = firstNext
            first, second = firstNext, secondNext
