class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n=len(nums)
        stack=[]
        ple1=[-1]*n
        for i in range(n):
            while stack and nums[stack[-1]]>nums[i]:
                stack.pop()
            ple1[i]=stack[-1] if stack else -1
            stack.append(i)
        stack=[]
        nle1=[n]*n
        for i in range(n-1,-1,-1):
            while stack and nums[stack[-1]]>=nums[i]:
                stack.pop()
            nle1[i]=stack[-1] if stack else n
            stack.append(i)
        result1=0
        for i in range(n):
            left1=i-ple1[i]
            right1=nle1[i]-i
            result1+=nums[i]*left1*right1
        stack=[]
        ple2=[-1]*n
        for i in range(n):
            while stack and nums[stack[-1]]<nums[i]:
                stack.pop()
            ple2[i]=stack[-1] if stack else -1
            stack.append(i)
        stack=[]
        nle2=[n]*n
        for i in range(n-1,-1,-1):
            while stack and nums[stack[-1]]<=nums[i]:
                stack.pop()
            nle2[i]=stack[-1] if stack else n
            stack.append(i)
        result2=0
        for i in range(n):
            left2=i-ple2[i]
            right2=nle2[i]-i
            result2+=nums[i]*left2*right2
        return result2-result1          