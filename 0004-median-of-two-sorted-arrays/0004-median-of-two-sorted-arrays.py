class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1=len(nums1)
        n2=len(nums2)
        n=n1+n2
        nums1+=nums2
        nums1.sort()
        # print(nums1[n//2])
        # print(      nums1[(n//2)-1])
        if(n%2==0):
            x= nums1[n//2]
            y=nums1[n//2-1]
            return (x+y)/2
        else:
            return nums1[n//2]
        