
from typing import List 

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        # 记录最大和最小
        f_max = [0] * n
        f_min = [0] * n

        f_max[0] = f_min[0] = nums[0]


        for i in range(1,n):
            tmp = nums[i]
            f_max[i] = max(f_max[i-1] * tmp,f_min[i-1] * tmp,tmp)
            f_min[i] = min(f_max[i-1] * tmp,f_min[i-1] * tmp,tmp)
            print(f"f_max: {f_max}, f_min: {f_min}")


        return max(f_max)



if __name__ == "__main__":
    s = Solution()
    print(s.maxProduct([2,3,-2,4]))  # 6
    print(s.maxProduct([-2,0,-1]))   # 0
    print(s.maxProduct([2,3,-1,4,3]))   # 12