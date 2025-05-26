class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        d={}
        for i in range(n):
            if nums[i] not in d:
                d[nums[i]]=i
            if target-nums[i] in d and d[target-nums[i]]!=i:
                return [i,d[target-nums[i]]]