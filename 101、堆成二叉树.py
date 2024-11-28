#Definition for a binary tree node.  
#TreeNode是leetcode预置的一个类  定义了一个类
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def ismirror(l,r):  #l是左节点，r是右节点。
            if not l and not r:
                return True
            if not l or not r:
                return False
            
            return (l.val==r.val) and ismirror(l.left,r.right) and ismirror(l.right,r.left)
        
        return ismirror(root,root)
        
# solution = Solution()
# print(solution.isSymmetric(root=[1,2,2,3,4,4,3]))  # 输出: True
"""
因为二叉树其实就是调用多次TreeNode去构造一个二叉树，不举具体例子了
"""