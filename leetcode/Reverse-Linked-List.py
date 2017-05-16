# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNod
        """
        newhead=None
        while head:
            newhead,head.next,head=head,newhead,head.next
        return newhead
leetcode
