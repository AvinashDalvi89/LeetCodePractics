# 4-> 2 -> 1 -> 9 given 2 as node to remove. as above other can't access previous node which is correct 
# because singly linked list we don't store predecessor. What can do is swap value of next of give node 
# to given node and change link to next of next of give node


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        nextNode = node.next 
        node.val = nextNode.val
        node.next = nextNode.next
