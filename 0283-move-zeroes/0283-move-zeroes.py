class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        i=j=0
        while i<n-1 and j<n-1:
            if nums[i]!=0:
                i+=1
                j+=1
            else:
                if nums[i+1]!=0:
                    nums[j],nums[i+1]=nums[i+1],nums[j]
                    i+=1
                    j+=1
                else:
                    i+=1
        