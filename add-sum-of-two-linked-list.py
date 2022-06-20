# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        p = l1
        q = l2
        while (p != None or q != None):
            x = p.val if p != None else 0
            y = q.val if q != None else 0
            sum = x+y+carry
            carry = sum/10
            curr.next = ListNode(sum % 10)
            curr = curr.next 
            p = p.next if p != None else p
            q = q.next if q != None else q
        if carry > 0 :
            curr.next = ListNode(carry)
        return dummy.next
        
