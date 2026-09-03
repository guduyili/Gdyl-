from functools import cache
from collections import Counter
class Solution:
    # 记忆化搜索
    def longestPalindromeSubseq(self, s: str) -> int:
        @cache
        def dfs(i:int,j:int)->int:
            if i > j:
                return 0
            elif i == j:
                return 1
            elif s[i] == s[j]:
                return dfs(i+1,j-1) +2
            # 枚举哪个不选
            return max(dfs(i+1,j),dfs(i,j-1))


        return dfs(0,len(s)-1)
    
    def longestPalindromeSubseq2(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        # i是从大到小
        for i in range(n-1,-1,-1):
            # 初始化 当只有一个时候为1
            dp[i][i] = 1
            # j是从小到大
            for j in range(i+1,n):
                if s[i] ==  s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j],dp[i][j-1])
        return dp[0][-1]

if __name__ == "__main__":
    s = Solution()
    print("\n记忆化搜索")
    print(s.longestPalindromeSubseq("bbbab"))
    print(s.longestPalindromeSubseq("cbbd"))
    print(s.longestPalindromeSubseq("a"))
    print(s.longestPalindromeSubseq("ac"))
    # n = len("bbbab")
    # dp = [[0] * n for _ in range(n)]
    # print(dp)
    print("\n动态规划")
    print(s.longestPalindromeSubseq2("bbbab"))
    print(s.longestPalindromeSubseq2("cbbd"))
    print(s.longestPalindromeSubseq2("a"))
    print(s.longestPalindromeSubseq2("ac"))
