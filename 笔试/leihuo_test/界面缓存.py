import sys
from collections import OrderedDict

def solve():
    # 一次性读取所有输入并按空白符分割
    data = sys.stdin.read().strip().split()
    if not data:
        return


    it = iter(data)

    # 读取 n, m, k
    n = int(next(it))   # 界面种类数
    m = int(next(it))   # 操作序列长度
    k = int(next(it))   # 缓存区容量

    # 读取每个界面是否可缓存，t[1..n]
    t = [0] + [int(next(it)) for _ in range(n)]

    # 状态标记数组 (1-indexed)
    open_flag = [False] * [n + 1]  # 当前界面是否已打开
    cache_flag = [False] * [n + 1]  # 当前界面是否已缓存

    # 使用有序字典维护顺序（插入顺序即为队列顺序）
    open_order = OrderedDict()  # 当前打开界面的顺序
    cache_order = OrderedDict()  # 当前缓存界面的顺序

    # 逐条处理操作：
    for _ in range(m):
        op = int(next(it))  # 操作类型
        x = int(next(it))   # 操作的界面编号
        # it = iter(data)

    

        if op == "open":
            # 情况1. 界面已经打开，放在open_order的末尾
            if  open_flag[x]:
                open_order.move_to_end(x)

            # 情况2： 界面已在缓存区 -> 从缓存取出 放在open_order的末尾
            if cache_flag[x]:
                cache_order.pop(x)          # 从缓存中移除
                cache_flag[x] = False
                open_order[x] = None        # 加入打开列表末尾
                open_flag[x] = True
            # 情况3： 界面未打开且不在缓存区
            else:
                open_flag[x] = True
                open_order[x] = None        # 加入打开列表末尾


        else:  # close 操作
        # 只有打开的界面才能被关闭
            if open_flag[x]:
                # 从打开列表中抹除
                open_order.pop(x)
                open_flag[x] = False

                # 根据是否可以缓存决定处理方式
                if t[x] == 1:  # 可缓存
                    # 可缓存：放入缓存区（FIFO）
                    # 如果缓存区已满，先淘汰最早进入的（队头
                    if len(cache_order) >= k:
                        oldest = next(iter(cache_order)) #获取队头键
                        cache_order.pop(oldest)          # 淘汰队头
                        cache_flag[oldest] = False           # 更新状态标记
                    # 将当前界面加入缓存区末尾
                    cache_order[x] = None
                    cache_flag[x] = True
                
                    