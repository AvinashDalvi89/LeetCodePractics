# Logic here is 
# 5 element if 2 times rotates then rotation will 2 times
# 3 element if 4 times rotates then answer will 1nd rotation means 1 times 
# 3 element if 5 times rotates then answer will 2nd rotation means 2 times 
# 3 element if 6 times rotates then answer will 0 rotation means directly return
# 3 element if 2 times rotates then answer will 2nd rotation means 2 times 
# first finding last node of list then pointing head to next of last node then finding module value rotation % size of list. Rotate for loop by size -k 
# assign last to next of last. after for loop end assign current node to next of last and next of last become null or None 
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None : return head 
        last = curr = head
        size = 1
        while last.next:
            last = last.next
            size += 1
        last.next = head
        k = k % size
        for i in range(0, size-k):
            last = last.next
        curr = last.next
        last.next = None
        return curr
            
