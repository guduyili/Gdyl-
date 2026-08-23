from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 使用前缀和 - 最小前缀和 ，并且更新最小前缀和
        pre_sum = 0
        min_pre_sum = 0
        ret = float('-inf')
        for i,n in enumerate(nums):
            # 最小前缀和在i>0后开始计算
            if i >0:
                min_pre_sum = min(min_pre_sum, pre_sum)
            pre_sum += n
            # 计算当前最大子数组和
            ret = max(ret,pre_sum - min_pre_sum)
        return ret

if __name__ == "__main__":
    s = Solution()
    print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
    print(s.maxSubArray([1]))
    print(s.maxSubArray([5,4,-1,7,8]))