class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x=nums[:n]
        y=nums[n:]
        z=[]
        for i in zip(x,y):
            p,q=i[0],i[1]
            z.append(p)
            z.append(q)
            
        return z