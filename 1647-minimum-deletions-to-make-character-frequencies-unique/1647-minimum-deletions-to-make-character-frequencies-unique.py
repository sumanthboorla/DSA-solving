class Solution:
    def minDeletions(self, s: str) -> int:
        d={}
        setting=set()
        ans=0
        for val in s:
            d[val]= d.get(val,0)+1
        
        for j in d.values():
            i=j
            if(i not in setting):
                setting.add(i)
            else:
                while(i>0 and i in setting):
                    i-=1
                    ans+=1
                    
                if(i>0):
                    setting.add(i)
        return ans
 