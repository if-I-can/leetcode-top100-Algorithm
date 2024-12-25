# Definition for a binary tree node.                                    #####  这个函数是在原二叉树上改的，所以并不需要return什么，只要启动这个函数就好了
# class TreeNode(object):                                               #####  这个题还是很有意义的，对理解二叉树和链表很有帮助
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        def zk(node):
            if not node:
                return None
            

            if node.left:
                zk(node.left)
                temp  = node.right
                node.right = node.left
                node.left = None


                while node.right:
                    node = node.right
                node.right = temp

                
            zk(node.right)

        zk(root)