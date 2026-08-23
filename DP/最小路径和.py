class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        m,n = len(grid),len(grid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]
        # 第一行 只能从左边来
        for j in range(1,n):
            dp[0][j] = dp[0][j-1] + grid[0][j] 
        # 第一列 只能从上边来
        for i in range(1,m):
            dp[i][0] = dp[i-1][0] + grid[i][0]

        # 其余部分
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = grid[i][j] + min(dp[i-1][j],dp[i][j-1])
        
        return dp[m-1][n-1]


if __name__ == "__main__":
    s = Solution()
    print(s.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
    print(s.minPathSum([[1,2,3],[4,5,6]]))