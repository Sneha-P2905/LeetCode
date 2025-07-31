class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        i=j=0
        while i<n and j<n:
            if nums[i]!=0:
                nums[j],nums[i]=nums[i],nums[j]
                i+=1
                j+=1
            else:
                i+=1
        return nums