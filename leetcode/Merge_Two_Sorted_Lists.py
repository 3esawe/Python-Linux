# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1    
        newNode = ListNode(0)
        p = newNode
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                p.next = l1
                l1 = l1.next
            elif l1.val >= l2.val:
                p.next= l2
                l2 = l2.next
            p = p.next
            if l1 is None:
                p.next = l2
                break
            if l2 is None:
                p.next = l1
                break
        return newNode.next
