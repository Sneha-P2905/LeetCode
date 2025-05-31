class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        count=0
        d={0:1}
        sum1=0
        for i in range(n):
            sum1 += nums[i]
            if sum1 - k in d:
                count += d[sum1 - k]
            if sum1 in d:
                d[sum1] += 1
            else:
                d[sum1] = 1
        return count
