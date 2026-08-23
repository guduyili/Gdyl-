from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        if not nums or k == 0:
            return []
        # 双端队列  右进左出  存储索引
        q = deque()

        ret = []

        for i, num in enumerate(nums):
            # 右进
            while q and nums[q[-1]] < num:
                q.pop()
            q.append(i)

            # 左出
            # 窗口最左边
            left = i - k + 1
            if q[0] < left:
                q.popleft()
            # 窗口内最大值
            if left >=0:
                ret.append(nums[q[0]])
        
        return ret
if __name__ == "__main__":
    solution = Solution()
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    result = solution.maxSlidingWindow(nums, k)
    print(result)  # 输出: [3,3,5,5,6,7]