class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        n=len(nums)
        min_stack=[0]*n
        min_stack[0]=nums[0]
        for i in range(1,n):
            min_stack[i]=min(min_stack[i-1],nums[i])
        stack=[]
        for j in range(n-1,-1,-1):
            if(nums[j]>min_stack[j]):
                while(stack and stack[-1]<=min_stack[j]):
                    stack.pop()
                if stack and stack[-1]<nums[j]:
                    return True
                stack.append(nums[j])
        return False
                
                    
        
        
        