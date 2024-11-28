# treeNode函数用来穿件字数，是leetcode自己定义的，从而确定传入参数root
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []
        
        def dfs(node):
            if node:
                dfs(node.left)  # 递归遍历左子树
                result.append(node.val)  # 访问根节点
                dfs(node.right)  # 递归遍历右子树
        
        dfs(root)
        return result