class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        n=len(nums1)
        if n%2==1:
            return nums1[(n+1)//2-1]
        else:
            mid=(n+1)/2
            i=int(mid)-1
            j=int(mid)
            return (nums1[i]+nums1[j])/2