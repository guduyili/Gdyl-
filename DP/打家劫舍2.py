from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp[n+1] = max(dp[n],dp[n-1]+nums)
        # 1.n 不被偷 dp[n] = dp[n-1] dp[n+1] = dp[n] + nums = dp[n-1] +nums
        # 合并为一种情况考虑
        # 2.n被偷 dp[n+1] = dp[n]+num不可取 dp[n+1] = dp[n]
        if len(nums) == 1:
            return nums[0]

        def rob1(nums) -> int:
            n = len(nums)
            dp = [0] * (n+1)
            # 分别切分nums[1:] 和 nums[:n-1]
            dp[0] = 0
            dp[1] = nums[0]
            for i in range(1,n):
                dp[i+1] =  max(dp[i],dp[i-1]+nums[i])
            max_1 = max(dp)
            return max_1
        # return rob1(nums[1:]) if rob1(nums[1:]) >= rob1(nums[:len(nums)-1]) else rob1(nums[:len(nums)-1])

        return max(rob1(nums[1:]),rob1(nums[:len(nums)-1]))

if __name__ == "__main__":
    nums = [2,7,9,3,2]
    solution = Solution()
    result = solution.rob(nums)
    print(result)  # Output: 11