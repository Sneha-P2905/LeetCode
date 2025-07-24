class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        dp=[[-1 for i in range(n+1)] for i in range(m+1)]
        return self.path(0,0,m,n,dp,grid)
    def path(self,ind1,ind2,m,n,dp,grid):
        if ind1>=m or ind2>=n:
            return float("inf")
        if ind1==m-1 and ind2==n-1:
            return grid[ind1][ind2]
        if dp[ind1][ind2]!=-1:
            return dp[ind1][ind2]
        right=grid[ind1][ind2]+self.path(ind1,ind2+1,m,n,dp,grid)
        bottom=grid[ind1][ind2]+self.path(ind1+1,ind2,m,n,dp,grid)
        dp[ind1][ind2]=min(right,bottom)
        return dp[ind1][ind2]