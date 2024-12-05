# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0 
        
        max_left_depth = self.maxDepth(root.left)
        max_right_depth = self.maxDepth(root.right)

        return max(max_left_depth,max_right_depth)+1