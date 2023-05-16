class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum1=0
        M=len(mat)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if(i==j):
                    sum1+=mat[i][j]
                elif i+j==M-1:
                    sum1=sum1+mat[i][j]
        return sum1
            
        