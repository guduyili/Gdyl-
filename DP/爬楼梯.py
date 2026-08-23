from functools import cache
class Solution:
    def climbStairs(self, n: int) -> int:
        # dp[n] = dp[n-1] + dp[n-2]
        # dp[1] = 1 dp[2] = 2 dp[0] = 1\
        @cache
        def dfs(n: int):
            if n <=1:
                return 1
            return dfs(n-1)+dfs(n-2)
        return  dfs(n)
if __name__ == '__main__':
    s = Solution()
    print(s.climbStairs(5))
    print(s.climbStairs(3))