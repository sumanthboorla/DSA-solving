class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        maxiweight=-1
        totalweight=0
        for weight in weights:
            maxiweight=max(maxiweight,weight)
            totalweight+=weight
            
        left,right=maxiweight,totalweight
        while(left<right):
            mid=(left+right)//2
            daysNeeded , currweight= 1,0
            for weight in weights:
                if currweight +weight >mid:
                    daysNeeded+=1
                    currweight=0
                currweight+=weight
            if(daysNeeded>days):
                left=mid+1
            else:
                right=mid
        return left
            
            
      