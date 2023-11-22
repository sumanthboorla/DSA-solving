class Solution {
    public int diagonalSum(int[][] mat) {
        int n= mat.length;
        int sum1=0;
        for(int i =0;i<mat.length;i++)
        {
            for(int j=0;j<mat[0].length;j++)
            {
                if(i==j)
                {
                    sum1+=mat[i][j];
                }
                if(i!=j && (i+j)==n-1)
                {
                    sum1+=mat[i][j];
                    
                }
            }
        }
        return sum1;
        
    }
}