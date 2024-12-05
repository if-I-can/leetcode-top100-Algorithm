# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if not root1 and not root2:
            return None
        if not root1:
            return root2
        if not root2:
            return root1
        
        val = root1.val+root2.val
        root = TreeNode(val)
        root.left = self.mergeTrees(root1.left,root2.left)
        root.right = self.mergeTrees(root1.right,root2.righht)
        return root
    