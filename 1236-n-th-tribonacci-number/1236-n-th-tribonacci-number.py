class Solution:
    def tribonacci(self, n: int) -> int:
        prev2=0
        prev1=1
        prev=1
        if n==0:
            return 0
        if n==1 or n==2:
            return 1
        for i in range(3,n+1):
            curr=prev+prev1+prev2
            prev2=prev1
            prev1=prev
            prev=curr
        return prev
        