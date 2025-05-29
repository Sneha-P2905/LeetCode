class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n=len(nums)
        if n<=10**5:
            s=set(nums)
            longest=0
            count=0
            x=0
            for nums in s:
                if nums-1 not in s:
                    x=nums
                    count=0
                    while x in s:
                        count+=1
                        x+=1
                    longest=max(longest,count)
            return longest            
        