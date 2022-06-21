# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA == None:
            return None
        if headB == None:
            return None
        ptrA = headA
        ptrB = headB
        sizeA = 0
        while headA:
            headA = headA.next
            sizeA += 1
        sizeB = 0 
        while headB:
            headB = headB.next
            sizeB += 1
        while sizeA != sizeB:
            if sizeA > sizeB:
                ptrA = ptrA.next
                sizeA -= 1
            elif sizeB > sizeA:
                ptrB = ptrB.next
                sizeB -= 1
            else:
                break
        while ptrA != ptrB:
            ptrA = ptrA.next
            ptrB = ptrB.next
        return ptrA
