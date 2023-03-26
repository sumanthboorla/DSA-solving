class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n=len(nums)
        sum1=sum(nums[:k])
        maxi_avg=sum1
        
        for i in range(1,n-k+1):
            sum1-=nums[i-1]
            sum1+=nums[i+k-1]
            maxi_avg=max(maxi_avg,sum1)
        return maxi_avg/k
    