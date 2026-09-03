import sys


def check_queue(u: str, v: str) -> bool:
    return u == v
def check_stack(u: str, v: str) -> bool:
    st = []         # 模拟栈
    # 指向目标出栈序列 V 的当前匹配下标
    j = 0
    for char in u:
        st.append(char)

        #贪心弹出 只要栈顶等于要输出的字符，立即弹出
        while st and st[-1] == v[j]:
            st.pop()
            j += 1
    # 如果栈为空，说明可以通过栈操作得到目标序列
    return len(st) == 0

import sys

def solve():
    input = sys.stdin.readline
    
    # 1. 安全读取 U（过滤空行与换行符）
    u = input()
    while u and u.strip() == '':
        u = input()
    if not u:
        return
    u = u.strip()
    
    # 2. 安全读取 V
    v = input()
    while v and v.strip() == '':
        v = input()
    v = v.strip()
    
    # 3. 分别进行两种数据结构的合法性判定
    is_q = check_queue(u, v)
    is_s = check_stack(u, v)
    
    # 4. 组合输出四种对应结果
    if is_q and is_s:
        sys.stdout.write("both\n")
    elif is_q:
        sys.stdout.write("queue\n")
    elif is_s:
        sys.stdout.write("stack\n")
    else:
        sys.stdout.write("neither\n")

if __name__ == '__main__':
    solve()