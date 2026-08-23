# 有效括号的变种题目，
# 其题目为八字符对应分别为bq,pd,e3,69,
# 这几对字符可以组成8就可以消掉，
# 现给出n组数据，每组包括一行length，k，分别为字符串长度和对应的可更改字符为以上八字符的次数。
# 第二行则为对应的字符串。给出该题的答案 

import sys


# 奇数长度特判： 若字符串长度 n 为奇数，无论如何修改都无法完全消除，
# 直接输出 No（或 false）。
# 区间 DP 求解最少修改次数：
# 设 dp[i][j] 为将子串 s[i...j] 变成完全合法消除串所需的最少修改字符数。消除外层匹配对：
# dp[i][j] = dp[i+1][j-1] + cost(s[i], s[j])
# 如果 (s[i], s[j]) 本身就是合法对，cost = 0；
# 如果通过修改其中一个字符就能配对（例如 s[i] 是合法左字符或 s[j] 是合法右字符），cost = 1；
# 如果两者都不是对应的一对且都需要修改，cost = 2。


# 区间分割合并： 枚举分割点 m（m - i 为奇数）：$$dp[i][j] = \min_{m=i+1, i+3, \dots}^{j-2} (dp[i][m] + dp[m+1][j])$$结果判定： 最终如果 $dp[0][n-1] \le k$，则输出 Yes（或 true），否则输出 No（或 false）。
def can_eliminate_string(s: str, k: int) -> bool:
    """
    判断字符串 s 是否能在最多修改 k 次的情况下完全消除。
    
    参数:
        s: 待判断的字符串
        k: 允许修改的最大字符次数
        
    返回:
        True: 可以完全消除
        False: 无法完全消除
    """
    n = len(s)
    
    # 1. 奇数长度不可能完全两两配对消除
    if n % 2 != 0:
        return False
    if n == 0:
        return True

    # 定义合法匹配对及左/右字符集合
    match_pair = {'b': 'q', 'p': 'd', 'e': '3', '6': '9'}
    left_chars = set(match_pair.keys())
    right_chars = set(match_pair.values())

    INF = float('inf')
    # dp[i][j] 表示将子串 s[i...j] 变成合法消除串所需的最小修改次数
    dp = [[INF] * n for _ in range(n)]


    def get_cost(c1: str, c2: str) -> int:
        if match_pair.get(c1) == c2:
            return 0  # 原本就是合法匹配（如 'b' 和 'q'）
        if c1 in left_chars or c2 in right_chars:
            return 1  # 仅需修改其中一个（如 'b' 和 'x' 改为 'b' 和 'q'）
        return 2      # 两个字符都需要修改（如 'x' 和 'y' 改为 'b' 和 'q'）

    # 区间DP 从小区间向着大区间递推,区间长度必须为偶数(2, 4, 6, ..., n)
    for length in range(2, n + 1, 2):
        for i in range(n - length + 1):
            j = i + length -1 

            # 策略1 s[i] 和 s[j]作为最外层的匹配对消掉
            inner_cost = 0 if length == 2 else dp[i +1][j -1]  # 内层子串的最小修改次数
            dp[i][j] = min(dp[i][j], inner_cost + get_cost(s[i], s[j]))

            # 策略 2: 枚举分割点 m，将区间拆分为 [i...m] 和 [m+1...j] 两个独立合法串
            # m 步长为 2 保证左右两部分长度均为偶数
            for m in range(i+1, j, 2):
                split_cost = dp[i][m] + dp[m+1][j]
                if split_cost < dp[i][j]:
                    dp[i][j] = split_cost
            
            # for m in range(i + 1, j, 2):
            #     split_cost = dp[i][m] + dp[m + 1][j]
            #     if split_cost < dp[i][j]:
            #         dp[i][j] = split_cost


    # print(dp)
    # 如果全局最小修改代价 <= k，则可以完全消除
    return dp[0][n - 1] <= k


def main():
    input = sys.stdin.readline
    line = input()
    while line.strip() == '':
        line = input()
    t = int(line)
    out = []
    for _ in range(t):
        line = input()
        while line.strip() == '':
            line = input()
        n, k = map(int, line.split())
        s = input().strip()
        out.append("Yes" if can_eliminate_string(s, k) else "No")
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()

# 10
# 2 0
# bq
# 2 0
# pq
# 4 0
# bqpd
# 4 1
# bpdq
# 6 1
# bqpd63
# 6 0
# bqpd63
# 8 0
# bqpd69e3
# 6 2
# bqpd6e
# 1 0
# 6
# 6 1
# bqpd69

# Yes
# No
# Yes
# Yes
# Yes
# No
# Yes
# Yes
# No
# Yes