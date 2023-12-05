class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        flat=[]
        re=[]
        for row in mat:
            for num in row:
                flat.append(num)  
        print(flat)
        if r*c != len(flat):
              return mat
        else:
            for x in range(r):
                re.append(flat[x*c : x*c+c])
            return re
            
            
                

        