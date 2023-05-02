class Solution:
    def arraySign(self, nums: List[int]) -> int:
        prod=1
        if(0 in nums):
            return 0
        
        else:
            for i in range(len(nums)):
                prod*=nums[i]
            if(prod>0):
                return 1
            elif(prod<0):
                return -1
                