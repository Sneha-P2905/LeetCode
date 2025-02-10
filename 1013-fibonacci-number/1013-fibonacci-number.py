class Solution:
    def fib(self, n: int) -> int:
        prev1=0
        prev=1
        if n==0 or n==1:
            return n
        for i in range(2,n+1):
            curr=prev+prev1
            prev1=prev
            prev=curr
        return prev
        