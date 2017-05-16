#Definition for singly-linked list.
 #class ListNode:
 #    def __init__(self, x):
 #        self.val = x
 #        self.next = None
class Solution(object):
    def removeElements(self, head, val):
        dummy=ListNode(0)
        dummy.next=head
        per=dummy
        cur=head
        while cur:
            if cur.val==val:
                per.next=cur.next
            else:
                per=cur
            cur=cur.next
        return dummy.next
# leetcode
