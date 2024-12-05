# Definition for a binary tree node.
"""
核心点是最大路径和是根节点的值和左右节点各自的最大路径和
"""

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.max_length = float('-inf')

        def helper(node):
            if not node:
                return 0

            depth_left = max(helper(node.left),0)
            depth_right = max(helper(node.right),0)

            the_length_of_current_node = depth_left+depth_right+ node.val

            self.max_length=  max(self.max_length, the_length_of_current_node)

            return node.val + max(depth_left,depth_right)
        
        helper(root)

        return self.max_length                    