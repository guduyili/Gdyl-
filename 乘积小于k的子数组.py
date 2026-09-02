
from typing import List
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<= 1:
            return 0
        
        ret = left = 0

        prod =1
        for right,n in enumerate(nums):
            prod *= n
            while prod >=k:
                # 移动left
                prod /= nums[left]
                left +=1
            ret += right - left +1
        return ret

if __name__ == "__main__":
    solution = Solution()
    nums = [10, 5, 2, 6]
    k = 100
    result = solution.numSubarrayProductLessThanK(nums, k)
    print(result)  # 输出: 8