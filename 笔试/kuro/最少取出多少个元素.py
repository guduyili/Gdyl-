# 至少需要取出多少个元素，才能通过修改取出的元素，使得「取出部分中 1 的数量」等于「剩余数组中 1 的数量」


class Solution:
    # def minTake(self, nums: list[int]) -> int:
    #     total = sum(nums)
    #     prefix = 0

    #     # k 表示取出前 k 个
    #     for k in range(len(nums) + 1):
    #         # 剩余部分 1 的数量
    #         remain = total - prefix

    #         # 取出的 k 个元素最多可以变成 k 个 1
    #         if remain <= k:
    #             return k

    #         # 为下一轮更新前缀 1 的数量
    #         prefix += nums[k]

    #     return len(nums)
    def minTake(self, nums: list[int]) -> int:
        # 前缀和
        #先是记录sum总和
        total = sum(nums)
        prefix = 0
        for k,num in enumerate(nums):
            # k就可以表示当前最多的1的数量
            # tmp = total - k
            # 剩余的1的数量
            total -= prefix
            if total<=k:
                return k
            prefix += num

        return len(nums)

    



if __name__ == "__main__":
    s = Solution()
    print(s.minTake([1, 0, 1, 0, 1]))  # 输出: 2
    print(s.minTake([0, 0, 0, 0]))     # 输出: 0
    print(s.minTake([1, 1, 1, 1]))     # 输出: 2
    print(s.minTake([1, 0, 0, 1, 0]))   # 输出: 1