# Reference explanation https://www.youtube.com/watch?v=-DzowlcaUmE&t=2378s just tweak some condition. This video about finding sub tree in binary tree. 
# Used same logic with little tweak for finding linked list in binary list
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubPath(self, head, root):
        """
        :type head: ListNode
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return
        if head == None:
            return True
        if self.identical(head,root):
            return True
        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
    
    def identical(self, head,root):
        if head == None: 
            return True
        
        if root == None:
            return False
        if root.val == head.val:
            print("identical"+str(root.val)+"---"+str(head.val))
            return self.identical(head.next, root.left) or self.identical(head.next, root.right)
        return False
