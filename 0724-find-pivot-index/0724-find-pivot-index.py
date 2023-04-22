class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum1=0
        for i in range(len(nums)):
            sum1+=nums[i]
        tmp=0
        for i in range(len(nums)):
            sum1-=nums[i]
            if(sum1==tmp):
                return i
            tmp+=nums[i]
        return -1
        
        
        
        
        
        
        
      