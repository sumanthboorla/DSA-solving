class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        maxi=0
        mini=float('inf')
        i=0
        while(i<n):
            mini=min(mini,prices[i])
            if(prices[i]>=mini):
                maxi=max(maxi,prices[i]-mini)
            i+=1
        return maxi
        