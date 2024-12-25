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
        def is_correct(node):
            if node.left > node.val or node.right < node.val:
                return False
            
            while node.left and node.right:
                is_correct(node.left)
                is_correct(node.right)
            
            return True
        return is_correct(root[0])