# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        length = len(lists)
        tempArr = []
        nextList = curr = ListNode()
        for i in range(length):
            
            temp = lists[i]
            curr.next = temp
            
            while temp:
                tempArr.append(temp.val)
                temp = temp.next
                curr = curr.next
    
        tempArr.sort()
        curr = nextList.next
        for i in range(len(tempArr)):
            curr.val = tempArr[i]
            curr = curr.next
        return nextList.next
        
