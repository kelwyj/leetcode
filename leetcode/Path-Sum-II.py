# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        result=[]
        self.helpper(root,sum,[],result)
        return result
        
    def helpper(self,root,sum,curr,result):
        if root is None:
            return
        if root.val==sum and root.left==None and root.right==None:
            result.append(curr+[root.val])
        self.helpper(root.left,sum-root.val,curr+[root.val],result)
        self.helpper(root.right,sum-root.val,curr+[root.val],result)

        
# leetcode
