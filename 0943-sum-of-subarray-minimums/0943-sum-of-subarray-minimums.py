class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n=len(arr)
        MOD=10**9+7
        stack=[]
        ple=[-1]*n
        for i in range(n):
            while stack and arr[stack[-1]]>arr[i]:
                stack.pop()
            ple[i]=stack[-1] if stack else -1
            stack.append(i)
        stack=[]
        nle=[n]*n
        for i in range(n-1,-1,-1):
            while stack and arr[stack[-1]]>=arr[i]:
                stack.pop()
            nle[i]=stack[-1] if stack else n
            stack.append(i)
        result=0
        for i in range(n):
            left=i-ple[i]
            right=nle[i]-i
            result+=arr[i]*left*right
        return result%MOD