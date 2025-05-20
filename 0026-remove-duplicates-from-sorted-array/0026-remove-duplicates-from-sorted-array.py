class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        j=0
        for i in range(n-1):
            if nums[i]==nums[i+1]:
                continue
            else:
                j+=1
                nums[j]=nums[i+1]
        del nums[j+1:]
        return len(nums)