class Solution:
    def triangleNumber(self, nums: list[int]) -> int:
        nums.sort()
        ret = 0
        for i in range(len(nums)):
            max_l = nums[i]
            left,right = 0, i-1
            while left < right:
                if nums[left] + nums[right] > max_l:
                    ret += right - left
                    right -= 1
                else:
                    left += 1

        return ret   


if __name__ == "__main__":
    solution = Solution()
    # nums = [2, 2, 3, 4]
    nums = input().split(" ")
    nums = [int(x) for x in nums]
    result = solution.triangleNumber(nums)
    print(result)  # 输出: 3