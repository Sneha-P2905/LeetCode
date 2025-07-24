class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        if grid[0][0]==1 or grid[m-1][n-1]==1:
            return 0
        dp=[[-1 for i in range(n+1)] for j in range(m+1)]
        return self.path(0,0,m,n,grid,dp)
    def path(self,ind1,ind2,m,n,grid,dp):
        if ind1>=m or ind2>=n:
            return 0
        if ind1==m-1 and ind2==n-1:
            return 1
        if grid[ind1][ind2]==1:
            return 0
        if dp[ind1][ind2]!=-1:
            return dp[ind1][ind2]
        right=self.path(ind1,ind2+1,m,n,grid,dp)
        bottom=self.path(ind1+1,ind2,m,n,grid,dp)
        dp[ind1][ind2]=right+bottom
        return dp[ind1][ind2]
        