from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        dp = [1] * n
        for i in range(len(nums)):
            for j in range(i):
                # j < i 
                # nums[j] < nums[i] 
                if nums[j] < nums[i]:
                    # 记录最长子序列长度
                    dp[i] = max(dp[i],dp[j]+1)
        return max(dp)

if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLIS([10,9,2,5,3,7,101,18]))
    print(s.lengthOfLIS([0,1,0,3,2,3]))
    print(s.lengthOfLIS([7,7,7,7,7,7,7]))