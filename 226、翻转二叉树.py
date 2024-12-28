# Definition for a binary tree node.
# class TreeNode(object):                                        #很简单的一个题。
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if not root:
            return None

        temp = root.right
        root.right = root.left
        root.left = temp

        self.invertTree(root.right)
        self.invertTree(root.left)
        
        return root