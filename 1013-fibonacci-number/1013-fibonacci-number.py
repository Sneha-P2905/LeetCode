class Solution:
    def fib(self, n: int) -> int:
        prev1=0
        prev=1
        if n==0:
            return 0
        for i in range(2,n+1):
            curr=prev+prev1
            prev1=prev
            prev=curr
        return prev
        