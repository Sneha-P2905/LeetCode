class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d={}
        for i,num in enumerate(numbers):
            result=target-num
            if result in d:
                return [d[result],i+1]
            d[num]=i+1
        return []        