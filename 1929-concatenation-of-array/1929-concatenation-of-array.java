class Solution {
    public int[] getConcatenation(int[] nums) {
            int n= nums.length;
            int arr [] = new int [n*2];
            int k=0;
            for (int i=0;i<arr.length;i++)
            {
                
                arr[i] = nums[k];
                k++;
                if(k==arr.length/2)
                {
                   k=0;    
                }
                
            }
        return arr;
    }
}