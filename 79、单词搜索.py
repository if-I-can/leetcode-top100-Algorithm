"""
这个运行时间会比较久一点，毕竟循环太多了。
"""

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def backtrack(i,j,k):

            #回溯终止条件
            if k == len(word):
                return True
            
            # 不符合直接跳出
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[k]:
                return False
            
            #若符合则说明，找到了第k个字符，现在要看他的下一个字符符不符合了
            temp = board[i][j]
            board[i][j] = "#"

            direct = ([1,0],[-1,0],[0,1],[0,-1])
            for m,n in direct:
                if backtrack(i+m,j+n,k+1):
                    return True
                
            board[i][j] = temp
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if backtrack(i,j,0):
                        return True

        return False            
