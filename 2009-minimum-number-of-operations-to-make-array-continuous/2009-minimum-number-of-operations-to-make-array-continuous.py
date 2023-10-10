class Solution:
    def minOperations(self, nums: List[int]) -> int:
        maxi = 0  
        count = 0  
        n = len(nums) - 1  
        l = 0  
        nums.sort()  
        i = 0
        while i < len(nums):
            if i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
                continue
            nums[l] = nums[i]
            l += 1
            i += 1

        i = 0
        j = 0
        while i < l:
            while j < l and (nums[j] - nums[i]) <= n:
                count += 1
                j += 1
            maxi = max(maxi, count)
            count -= 1
            i += 1

        return len(nums) - maxi
            
        