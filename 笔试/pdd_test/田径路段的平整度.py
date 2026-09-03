# 二分查找与贪心与差分数组检验
import sys

def solve():
    # 读取第一行输入：N（段数）, m（每次修改长度）, k（修改次数）
    line1 = sys.stdin.readline().split()
    if not line1:
        return
    N, m, k = map(int, line1)
    
    # 读取第二行输入：各段初始平整度
    arr = list(map(int, sys.stdin.readline().split()))
   
    def check(target: int):
        # 累计消耗的操作次数
        has_used = 0
        # 当前位置 i 受到的累计增量
        current_add = 0
        # 记录增量失效位置的差分数组
        # 方式为diff[i+m] -= 
        diff = [0] * (N+1)
        
        # 贪心计算
        for i in range(N):
            # 1. 结算过期增量：如果之前的某些操作在位置 i 到期，更新 current_add
            current_add += diff[i]
            # 实际高度
            val=current_add + arr[i]
            
            # 3. 如果当前高度不达标，贪心补齐
            if val < target:
                tmp_diff = target - val
                has_used += tmp_diff
                
                # 剪枝：如果总消耗已超过 k，无需继续计算，直接判定不可行
                if has_used > k:
                    return False
                
                # 4. 施加操作：即时生效
                current_add += tmp_diff
                
                # 5. 设置失效点：此操作的影响在 i + m 处结束
                if i+m < N:
                    diff[i+m] -= tmp_diff
        # k未用完
        return has_used <= k
    	

    # 二分查找
    low = min(arr)
    high = low + k
    ret = low
    
    
    while low <= high:
        mid = (low+high) //2
        # mid 可行，将全数组变为mid而k未用完，因此实际上存在比其更大的最小值,尝试寻找更大的最小值
        if check(mid):
            ret = mid
            low =  mid+1
   		# mid 不可行，不存在将全数组变为mid而k未用完
        else:
            high  = mid-1
    print(ret)
    
    
    
if __name__ == '__main__':
    solve()