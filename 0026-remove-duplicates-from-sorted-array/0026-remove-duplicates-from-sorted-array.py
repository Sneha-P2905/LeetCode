class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j=0
        i=0
        n=len(nums)
        while i<n-1:
            if nums[i]==nums[i+1]:
                i+=1
            else:
                j+=1
                nums[j]=nums[i+1]
                i+=1
        del nums[j+1:]
        return len(nums)