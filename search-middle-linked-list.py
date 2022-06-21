# Given the head of a singly linked list, return the middle node of the linked list.

# If there are two middle nodes, return the second middle node.
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp = head
        size = 0
        while temp:
            temp = temp.next 
            size += 1
        rotation = size/2
        if size % 2 == 0 : 
            rotation = (size/2)-1
        for i in range(rotation):
            head = head.next 
        return head.next if size % 2 == 0 else head
