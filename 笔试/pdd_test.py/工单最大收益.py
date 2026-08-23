import sys
from bisect import bisect_right



# 手写二分：在 jobs[0...right_bound-1] 中查找结束时间 <= target 的最大 1-based 下标
def find_last_non_conflict(right_bound, target):
    left, right = 0, right_bound - 1
    res = 0  # 默认 0 表示没有找到兼容的前驱
    while left <= right:
        mid = (left + right) // 2
        if jobs[mid][1] <= target:
            res = mid + 1  # 记录当前满足条件的 1-based 下标
            left = mid + 1 # 尝试往右找更大的下标
        else:
            right = mid - 1 # 结束时间偏大，向左收缩
    return res


def solve():
    input = sys.stdin.readline
    
    line = input()
    while line and line.strip() == '':
        line = input()
    if not line:
        return
        
    m = int(line.strip())
    jobs = []
    for _ in range(m):
        row = input()
        while row and row.strip() == '':
            row = input()
        if not row:
            break
        a, b, w = map(int, row.split())
        jobs.append((a, b, w))
        
    # 按结束时间 b 从小到大排序
    # jobs.sort(key=lambda x: x[1])
    jobs.sort(key=lambda x: x[1])
    
    # 提取所有结束时间用于二分查找
    ends = [job[1] for job in jobs]
    
    # dp[i] 表示前 i 个工单的最大收益 (1-indexed)
    dp = [0] * (m + 1)
    
    for i in range(1, m + 1):
        a, b, w = jobs[i - 1]
        
        # 二分查找满足 ends[k-1] <= a 的最大下标 k
        # bisect_right 查找 <= a 的元素个数，正好对应 1-indexed 下的 k
        k = bisect_right(ends, a)
        
        # 转移方程：不选 vs 选
        dp[i] = max(dp[i - 1], w + dp[k])
        
    sys.stdout.write(str(dp[m]) + '\n')

if __name__ == '__main__':
    solve()