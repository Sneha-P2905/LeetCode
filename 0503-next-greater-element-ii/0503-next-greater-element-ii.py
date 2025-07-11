class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack=[]
        n=len(nums)
        res=[-1]*n
        for i in range(2*n):
            curr=nums[i%n]
            while stack and nums[stack[-1]]<curr:
                ind=stack.pop()
                res[ind]=curr
            if i<n:
                stack.append(i)
        return res