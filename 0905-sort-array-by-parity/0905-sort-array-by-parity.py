class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        s=[]
        s2=[]
        nums.sort()
        for i in nums:
            if(i%2==0):
                s.append(i)
            else:
                s2.append(i)
        s.extend(s2)
        return s
                
            
        