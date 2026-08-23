class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0 or x>0 and x %10 ==0:
            return False
        tmp = 0
        while x // 10 > tmp:
            tmp = tmp *10 + x % 10
            x = x //10
        return tmp == x//10 or tmp == x
        
        

        

if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome(121))
    print(s.isPalindrome(-121))
    print(s.isPalindrome(10))
    print(s.isPalindrome(12321))
    print(s.isPalindrome(11))