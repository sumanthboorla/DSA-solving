class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        l=[]
        for i in range(len(candies)):
            sum1=0
            sum1+=candies[i]+extraCandies
            for j in range(len(candies)):
                if(sum1>=max(candies)):
                    l.append(True)
                    break
                else:
                    l.append(False)
                    break
        return l
                    