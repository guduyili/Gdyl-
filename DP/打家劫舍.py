
from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp[n+1] = max(dp[n],dp[n-1]+nums)
        # 1.n 不被偷 dp[n] = dp[n-1] dp[n+1] = dp[n] + nums = dp[n-1] +nums
        # 合并为一种情况考虑
        # 2.n被偷 dp[n+1] = dp[n]+num不可取 dp[n+1] = dp[n]
        # cur,pre = 0,0
        # for num in nums:
        #     cur,pre = max(pre+num,cur),cur
        # return cur
        n = len(nums)
        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = nums[0]
        for i in range(1,n):
            dp[i+1] = max(dp[i],dp[i-1]+nums[i])
        return max(dp)


if __name__ == "__main__":
    nums = [2,7,9,3,1]
    solution = Solution()
    result = solution.rob(nums)
    print(result)  # Output: 12