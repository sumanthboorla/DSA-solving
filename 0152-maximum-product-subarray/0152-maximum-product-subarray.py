class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n= len(nums)
        res=nums[0]
        l=1
        r=1
        for i in range(len(nums)):
            l=(l)*nums[i]
            r =(r) *nums[n-1-i]
            res = max(res,max(l,r))
            if(l==0):
                l= 1
            if(r==0):
                r=1
        
        return res
                
            
        
                
        