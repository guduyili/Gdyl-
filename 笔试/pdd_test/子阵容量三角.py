# x ^ y ^ z = 0    x^y == z
# x + y >= z ==
# x + y >=  x ^ y == 
# x & y != 0

# 已知 x + y = (x ^ y)[本位和] + 2 * (x & y)[进位值]。代入 z = x ^ y，
# 得到 x + y = z + 2(x & y)。满足三角形条件 x + y > z 等价于：2(x & y) > 0 (x & y) != 0


import sys

def solve():
    input = sys.stdin.readline

    # 过滤可能存在的前置空行并读取 n
    line = input()
    while line is not None and line.strip() == "":
        line = input()

    if not line:
        return

    n = int(line.strip())

    ans = 0
    # 枚举 x 和 y (1 <= x <= y <= n)
    for x in range(1, n + 1):
        for y in range(x, n + 1):
            z = x ^ y
            # 满足 y <= z <= n 且构成三角形 (x & y != 0)
            if y <= z <= n and (x & y) != 0:
                ans += 1

    sys.stdout.write(str(ans) + "\n")


if __name__ == "__main__":
    solve()