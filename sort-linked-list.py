# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummyArr = []
        temp = head 
        while temp:
            dummyArr.append(temp.val)
            temp = temp.next
            
        dummyArr.sort()
        sortList = head
        i = 0
        while sortList:
            sortList.val = dummyArr[i]
            sortList = sortList.next
            i += 1
        return head
