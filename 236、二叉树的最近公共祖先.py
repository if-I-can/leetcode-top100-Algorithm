"""
还不错的一个题
递归,思想是这样的,递归左右子树,如果左子树和右子树都能找到一个root 使其都满足或者root=p/q就行，且这里要知道，p和q是不会相等的且一定存在， 这是题目的设定
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or root == p or root ==q:
            return root                    #这里本来是我疑惑的点，但其实如果遍历到最后的，root其实就是None了，不影响的，对应于p，q在同一边子树
        
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
        
        if left and right:
            return root                    ##### 不断向上返回
        
        return left if left else right
        
        