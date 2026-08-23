class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 双指针 滑动窗口
        from collections import Counter
        need = Counter(t)
        # 记录窗口中字符的频率
        record = Counter()
        # 初始化左指针
        left = 0
        ret_l,ret_r = -1,len(s) 
        for right,char in enumerate(s):
            # 先录入S中的字符
            record[char] += 1

            # 如果当前字符在T中，并且窗口中该字符的频率小于等于T中该字符的频率，
            # 则说明窗口中还缺少该字符
            while record >= need:
                # 如果当前窗口的长度小于之前记录的最小窗口长度，则更新最小窗口的左右指针
                if right - left < ret_r - ret_l:
                    ret_l,ret_r = left,right
                record[s[left]] -= 1
                left += 1
        # 如果ret_r没有更新，说明没有找到符合条件的窗口，返回空字符串
        if ret_l == -1:
            return ""
        
        return s[ret_l:ret_r+1]


if __name__ == "__main__":
    s = "ADOBECODEBANC"
    t = "ABC"

    solution = Solution()
    result = solution.minWindow(s, t)
    print(result)  # Output: "BANC"