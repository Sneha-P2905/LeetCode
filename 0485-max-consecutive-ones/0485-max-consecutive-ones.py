class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n=len(nums)
        Max=0
        count=0
        i=0
        for i in range(n):
            if nums[i]==1:
                count+=1
                Max=max(count,Max)
            else:
                count=0
        return Max
        