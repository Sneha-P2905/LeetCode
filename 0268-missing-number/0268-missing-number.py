class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        Max=max(nums)
        Hash=[0]*(Max+1)
        for i in nums:
            Hash[i]+=1
        for i in range(len(Hash)):
            if Hash[i]==0:
                return i
        return len(Hash)

        