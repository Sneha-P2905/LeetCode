class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i,num in enumerate(nums):
            result=target-num
            if result in d:
                return [d[result],i]
            d[num]=i
        return []