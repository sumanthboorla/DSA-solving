class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        re=0
        for val in nums:
            if val-1 not in nums:
                count=val
                while(count in nums):
                    count+=1
                re=max(re,count-val)
        return re