class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 中心扩散法
        ## 偶数和奇数统一计算
        n = len(s)
        ret_l,ret_r = 0,0
        for i in range(2 *n-1):
            l = i // 2
            r = (i+1) //2 

            while  l>=0 and r <n and s[l] == s[r]:
                l -=1 
                r += 1
            # r-1 - (l+1) + 1 = r - l - 1
            if r-l-1 > ret_r-ret_l:
                ret_l,ret_r = l+1,r-1

        return s[ret_l:ret_r+1]


if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindrome("babad"))
    print(s.longestPalindrome("cbbd"))
    print(s.longestPalindrome("a"))
    print(s.longestPalindrome("ac"))