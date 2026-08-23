import math
import sys

# hp
# a_mask 记录魔法1的使用次数
# b_mask 记录魔法2的使用次数
# used3 记录魔法3是否使用过
# used4 记录魔法4是否使用过
# last_amp 记录上一次使用的魔法的增幅
# last_amp = 0 表示上一次没有使用增幅魔法
def dfs(hp,a_mask,b_mask,used3,used4,last_amp,n,m,p,q,a,b) -> bool:
    if hp < 1:
        return True
    # 分情况讨论
    # 上一步使用的增幅魔法
    if last_amp > 0:
        # 按次数计算魔法2
        for i in range(m):
			# 第i位是否为0
            if not((b_mask >>i )& 1):
                damge = last_amp * b[i]
                if dfs(hp-damge,a_mask,b_mask|(1<<i),used3,used4,0,n,m,p,q,a,b):
                    return True
        # 增幅魔法3
        if not used3:
            damge = last_amp * ((p * hp) // q)
            if dfs(hp-damge,a_mask,b_mask,True,used4,0,n,m,p,q,a,b):
                    return True
        # 增幅魔法4
        if not used4:
            damge = last_amp * math.isqrt(hp)
            if dfs(hp-damge,a_mask,b_mask,used3,True,0,n,m,p,q,a,b):
                    return True
    # 上一次未使用增幅魔法 判断是否能使用增幅魔法
    tmp_amp = (b_mask != (1 << m) - 1) or not(used3) or not(used4)
    if tmp_amp:
         # 按次数计算魔法1
        for i in range(n):
			# 第i位是否为0
            if not((a_mask >>i )& 1):
                last_amp = a[i]
                if dfs(hp,a_mask|(1<<i),b_mask,used3,used4,last_amp,n,m,p,q,a,b):
                    return True
    # 无增幅使用魔法2
    for i in range(m):
        # 第i位是否为0
        if not((b_mask >>i )& 1):
            damge = b[i]
            if dfs(hp-damge,a_mask,b_mask|(1<<i),used3,used4,0,n,m,p,q,a,b):
                return True
    # 无增幅魔法3
    if not used3:
        damge = (p * hp) // q
        if dfs(hp-damge,a_mask,b_mask,True,used4,0,n,m,p,q,a,b):
                return True
    # 无增幅魔法4
    if not used4:
        damge =math.isqrt(hp)
        if dfs(hp-damge,a_mask,b_mask,used3,True,0,n,m,p,q,a,b):
                return True 
    return False


def main():
    input = sys.stdin.readline
    T = int(input())
    results = []
    for _ in range(T):
        n,m,p,q,y = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))

        hp = 10 ** 9 + y # 初始血量（题目中 x = 10^9，输入
        if dfs(hp, 0, 0, False, False, 0, n, m, p, q, a, b):
            results.append("YES")
        else:
            results.append("NO")

    sys.stdout.write("\n".join(results))
    # sys.stdout.write("\n".join(results))

if __name__ == "__main__":
    main()