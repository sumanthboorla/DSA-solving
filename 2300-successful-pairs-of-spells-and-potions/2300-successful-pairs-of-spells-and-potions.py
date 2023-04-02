class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        
        n=len(spells)
        m=len(potions)
        x=[0]*n
        potions.sort()        
        for i in range(n):
            spell=spells[i]
            l=0
            r=m-1
            while(l<=r):
                mid=l+(r-l)//2
                p=spell*potions[mid]
                if(p>=success):
                    r=mid-1
                else:
                    l=mid+1
            x[i]=m-l
        return x
                
            #     p=spells[i]*potions[j]
            #     if(p>=success):
            #         count+=1
            #     j+=1
            # x.append(count)
#         return x
        

        