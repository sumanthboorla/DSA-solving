class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d={}
        for i in range(len(nums)):
            if(nums[i] not in d):
                d[nums[i]]=1
            else:
                d[nums[i]]+=1
    
        
        l=[]
        for i,j in d.items():
            if(j>len(nums)//3):
                l.append(i)
            else:
                pass
        return l
            