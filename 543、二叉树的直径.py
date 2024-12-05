# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        
        self.diameter = 0
        def depth(node):
            if not node:
                return None
            
            depth_left = depth(node.left)
            depth_right = depth(node.right)

            self.diameter = max(self.diameter,depth_left+depth_right)

            return (1 + depth_right+depth_left)
        
        depth(root)

        return self.diameter