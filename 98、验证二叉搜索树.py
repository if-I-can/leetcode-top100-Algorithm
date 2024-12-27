# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def is_correct(node,low,high):

            if not node:
                return True
            
            if node.val <= low or node.val >= high:
                return False
            
            return is_correct(node.left,low,node.val) and is_correct(node.right,node.val,high)
        
        return is_correct(root,float('-inf'),float('inf'))