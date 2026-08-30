class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
            nums.sort()
            ret = []
            length = len(nums)
            # 遍历每个数字，作为三元组的第一个元素
            # 使用双指针技术来寻找另外两个元素
            for i in range(len(nums) -2):
                 # 判断三种情况
                 if nums[i] > 0:
                      break
                 # 加最大两数小于0
                 if nums[i] + nums[length-1] + nums[length-2] < 0:
                      continue
                 # 加最小两数大于0
                 if nums[i] + nums[i+1] + nums[i+2] > 0:
                      break
                 # 跳过重复的数字
                 if i > 0 and nums[i] == nums[i-1]:
                      continue

                 # 锁定一个数字后，使用双指针寻找另外两个数字
                 left, right = i + 1, length - 1
                 while left < right:                           
                      if nums[i] + nums[left] + nums[right] < 0:
                           left += 1
                      elif nums[i] + nums[left] + nums[right] > 0:
                           right -= 1

                      else:
                         # 如果 j > i+1 且 nums[j] == nums[j-1] 则是重复的
                         if left == i +1 or nums[left] != nums[left-1]:
                              ret.append([nums[i], nums[left], nums[right]])

                              left += 1
                              right -= 1
          
            return ret


if __name__ == "__main__":
    solution = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    result = solution.threeSum(nums)
    print(result)  # 输出: [[-1, -1, 2], [-1, 0, 1]]



def func(nums:list[int]):
     nums.sort()
     ret = []
     n = len(nums)
     for i in range(n-2):
          tmp = nums[i]
          # 当前等于之前出现过的跳过
          if i > 0 and tmp == nums[i-1]:
               continue
          # 当前大于0，后面不可能有和为0的组合
          # tmp + nums[i+1] + nums[i+2] > 0 break
          if tmp + nums[i+1] + nums[i+2] > 0:
                break
          # tmp + nums[n-2] + nums[n-1] < 0 break
          if tmp + nums[n-2] + nums[n-1] < 0:
               continue
          # 使用双指针寻找另外两个数字
          l,r = i+1, n-1
          while l < r:
               s = tmp + nums[j] + nums[k]
               if s > 0:
                    k -= 1

               elif s < 0:
                    j += 1

               else:
                    # 如果 j > i+1 且 nums[j] == nums[j-1] 则是重复的
                    if j == i+1 or nums[j] != nums[j-1]:
                        ret.append([tmp,nums[j],nums[k]])
                    
                    # 否则 左右指针同步移动
                    j += 1
                    k -= 1
     return ret