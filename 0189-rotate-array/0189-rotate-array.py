class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k=k%n
        a=nums[n-k:]
        b=nums[:n-k]
        nums[n-k:]=a[::-1]
        nums[:n-k]=b[::-1]
        nums[:]=nums[::-1]
        
        