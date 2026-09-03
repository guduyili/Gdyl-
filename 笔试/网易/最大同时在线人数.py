# 题目：最大同时在线人数

# 给定一个二维数组 intervals，其中 intervals[i] = [login_i, logout_i] 表示第 i 个用户的登录时间和登出时间。

# 规定用户在区间 [login_i, logout_i) 内处于在线状态，即：

# 在 login_i 时刻开始在线；
# 在 logout_i 时刻已经离线。

# 请你计算任意时刻的 最大同时在线人数。



# intervals = [[1, 4], [2, 5], [3, 6]]


# record = [0] * 100000  # 假设时间范围在0到99999之间

# for interval in intervals:
#     for i in range(interval[0], interval[1]):
#         record[i] += 1

# print(max(record))  # 输出最大同时在线人数


def max_online(intervals):
    events = []

    for login, logout in intervals:
        events.append((login, 1))    # 登录 +1
        events.append((logout, -1))  # 登出 -1

    # 按时间排序
    # 同一时刻先处理 logout(-1)，再处理 login(+1)
    events.sort()
    print(events)  # 输出事件列表，便于调试

    cur = 0
    ans = 0

    for time, change in events:
        cur += change
        ans = max(ans, cur)

    return ans


intervals = [[1, 4], [2, 5], [3, 6]]
print(max_online(intervals))  # 3