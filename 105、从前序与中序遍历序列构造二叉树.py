# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        def build(pre_start,start,end):

            if pre_start>=len(preorder) or start > end:
                return None
            
            root_val = preorder[pre_start]
            root = TreeNode(root_val)
            root_index = index_order[root_val]

            root.left = build(pre_start+1,start,root_index-1)
            root.right = build(pre_start+1+(root_index-start),root_index+1,end)
        
            return root

        index_order = {value:index for index, value in enumerate(inorder)}
        return build(0,0,len(inorder)-1)
