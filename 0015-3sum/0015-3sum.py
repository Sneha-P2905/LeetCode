class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        arr=[]
        for i in range(n):
            j=i+1
            k=n-1
            if i>0 and nums[i]==nums[i-1]:
                continue
            while j<k:
                total=nums[i]+nums[j]+nums[k]
                if total==0:
                    arr.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                    while j<k and nums[k]==nums[k+1]:
                        k-=1
                if total<0:
                    j+=1
                if total>0:
                    k-=1
        return arr
