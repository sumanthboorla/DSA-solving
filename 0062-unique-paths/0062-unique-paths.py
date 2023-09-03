class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grids=[[1 for i in range(n)] for j in range(m)]
        
        for i in range(1,m):
            for j in range(1,n):
                grids[i][j]=grids[i-1][j]+grids[i][j-1]
                
        return grids[-1][-1]
        