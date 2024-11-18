### 旋转90°图像，原理如下：先求转置矩阵，然后在对每一行翻转

class Solution():
    def rotate(self,matric):

        for i in range(len(matric)):
            for j in range(i+1,len(matric)):
                matric[i][j],matric[j][i] = matric[j][i], matric[i][j]
        
        for k in range(len(matric)):
            matric[k].reverse()
        return matric


tem = Solution()
print(tem.rotate(matric = [[1,2,3],[4,5,6],[7,8,9]]))
