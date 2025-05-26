class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        count=0
        el=0
        for i in range(n):
            if count==0:
                el=nums[i]
            if nums[i]==el:
                count+=1
            if nums[i]!=el:
                count-=1
        count=0
        for j in range(n):
            if nums[j]==el:
                count+=1
        if count>n/2:
            return el
        