class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[-1 for i in range(n+1)] for j in range(m+1)]
        return self.path(0,0,m,n,dp)
    def path(self,ind1,ind2,m,n,dp):
        if ind1>=m or ind2>=n:
            return 0
        if ind1==m-1 and ind2==n-1:
            return 1
        if dp[ind1][ind2]!=-1:
            return dp[ind1][ind2]
        right=self.path(ind1,ind2+1,m,n,dp)
        bottom=self.path(ind1+1,ind2,m,n,dp)
        dp[ind1][ind2]=right+bottom
        return dp[ind1][ind2]
    