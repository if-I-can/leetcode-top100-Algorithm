"""
题还是要多看点，多练，没多难，做这个题要了解题目和底层逻辑，即用回溯算法从下往上从右往左
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def convertBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        self.num = 0
        def bt(node):
            if not node:
                return
            
            bt(node.right)
            self.num += node.val
            node.val = self.num
            bt(node.left)


        bt(root,0)
        return root
        