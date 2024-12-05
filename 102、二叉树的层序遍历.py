# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        result = []
        queue = deque([root])
        while queue:
            tep = []
            len_node = len(queue)
            for _ in range(len_node):
                node = queue.popleft()
                tep.append(node.val)
                if node.left():
                    queue.append(node.left)
                if node.right():
                    queue.append(node.right)
            result.append(tep)

        return result