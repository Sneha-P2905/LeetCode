class Solution:
    def climbStairs(self, n: int) -> int:
        self.prev1=1
        self.prev=1
        for i in range(2,n+1):
            self.curr=self.prev+self.prev1
            self.prev1=self.prev
            self.prev=self.curr
        return self.prev
        