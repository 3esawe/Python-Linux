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
        newNode = ListNode(None)
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                newNode.next = l1
            elif l1.val >= l2.val:
                newNode.next = l2
            else:
                l1 = l1.next
                l2 = l2.next
            return newNode
