class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        
        matrix=[]
        if(m*n==len(original)):
            ind=0
            for i in range(m):
                t=[]
                for j in range(0,n):
                    t.append(original[ind])
                    ind+=1
                matrix.append(t)
                
        return matrix
                