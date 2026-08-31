from typing import List
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 关注 gas总和是否大于cost总和 大于则有解 小于则-1
        ret = min_ret = 0

        tmp = 0
        for i, (g,c) in enumerate(zip(gas,cost)):
            tmp += g - c
            if tmp < min_ret:
                # 更新最小油量
                min_ret = tmp
                ret = i+1
        
        return -1 if tmp < 0 else ret



if __name__ == "__main__":
    s = Solution()
    
    print(s.canCompleteCircuit([1,2,3,4,5],[3,4,5,1,2]))    # 3
    print(s.canCompleteCircuit([2,3,4],[3,4,3]))            # -1