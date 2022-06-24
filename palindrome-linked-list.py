# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        dummyArr = []
        temp = head
        while temp:
            dummyArr.append(temp.val)
            temp = temp.next
        reverse = dummyArr[::-1]
        if(dummyArr == reverse):
            return True
        else:
            return False
