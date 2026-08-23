import sys
import math
# (x + y)^2 - x^2 - y^2 = 2xy => xy = (x + y)^2 - (x^2 + y^2) /2

def main():
    input = sys.stdin.readline
    if not input:
        return

    # 2. 常量定义
    MOD = 10**9 + 7
    # 在模运算下，除以 2 等价于乘以 2 的模逆元 (inv2)
    # 根据费马小定理或公式 (MOD + 1) // 2，可得 2 的逆元为 500000004
    INV2 = (MOD + 1) // 2
    

    num = int(input())
    ret = []
    for _ in range(num):
        n = int(input().split()[0])
        l1 = list(map(int, input().split()))
        sum_1 = 0
        sum_2 = 0
        # print(n)
        # print(l1)
        for i in range(n):
            sum_1 = (sum_1 + l1[i]) % MOD
            sum_2 = (sum_2 + l1[i] * l1[i]) % MOD
        # 使用逆元避免浮点数运算，确保结果在模运算下正确
        tmp = (sum_1 * sum_1 - sum_2) % MOD
        tmp = (tmp * INV2) % MOD
        ret.append(tmp)

    sys.stdout.write("\n".join(map(str,ret)) + "\n")
    return ret



if __name__ == "__main__":
    main()