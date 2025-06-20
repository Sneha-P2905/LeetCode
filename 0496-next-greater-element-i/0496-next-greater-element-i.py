class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        for i in range(len(nums1)):
            n=nums2.index(nums1[i])
            found=False
            for j in range(n,len(nums2)):
                if nums2[j]>nums1[i]:
                    ans.append(nums2[j])
                    found=True
                    break
            if not found:
                ans.append(-1)
        return ans