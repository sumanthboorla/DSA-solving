class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2

            if nums[left] == target or nums[mid] == target or nums[right] == target:
                return True

            if nums[left] < nums[mid]: # Left side sorded
                if nums[left] < target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] < nums[right]: # Right side sorted
                if nums[mid] < target < nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                left, right = left + 1, right - 1
        return False
    

        