# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """
        def bt(node,current_path):
            if not node:
                return 0
            
            current_path.append(node.val)
            count = 0
            path_num = 0

            for i in range(len(current_path)-1,-1,-1):
                path_num += current_path[i]
                if path_num == targetSum:
                    count += 1
                
            count += bt(node.left,current_path)
            count += bt(node.right,current_path)

            current_path.pop()

            return count

        return bt(root,[])


