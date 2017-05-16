#Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result=0
        return self.helpper(root,result)

    def helpper(self,root,result):
        if root==None:return 0
        result=10*result+root.val
        if root.left==None and root.right==None:
            return result
        return self.helpper(root.left,result)+self.helpper(root.right,result)
# leetcode
