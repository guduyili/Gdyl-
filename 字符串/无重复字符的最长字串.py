class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        # 初始化左端点滑动窗口
        left = 0
        # 存长度和char的位置
        cnt_t = {}
        ret = 0

        for r,char in enumerate(s):
            # 重复字符 更新左端点 cnt_t[char]+1为上一个该字符的端点
            if char in cnt_t:
                left = max(left,cnt_t[char]+1)
            # 存长度和char的位置
            cnt_t[char] = r

            ret = max(ret,r-left+1)

        return ret

if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))
    print(s.lengthOfLongestSubstring("bbbbb"))
    print(s.lengthOfLongestSubstring("pwwkew"))
    print(s.lengthOfLongestSubstring(""))