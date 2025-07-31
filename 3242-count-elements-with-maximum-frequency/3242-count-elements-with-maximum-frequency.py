class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        Hash=[0]*(max(nums)+1)
        Hash[0]=float("-inf")
        for i in nums:
            Hash[i]+=1
        Max=max(Hash)
        arr=[]
        for i in range(len(Hash)):
            if Hash[i]==Max:
                arr.append(i)
        return len(arr)*Max
        