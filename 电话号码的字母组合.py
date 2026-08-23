MAPPING = "", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return list()

        # phoneMap = {
        #     "2": "abc",
        #     "3": "def",
        #     "4": "ghi",
        #     "5": "jkl",
        #     "6": "mno",
        #     "7": "pqrs",
        #     "8": "tuv",
        #     "9": "wxyz",
        # }
        
        n = len(digits)
        ret = []
        ret1 = []
        path = [''] * n

        # dfs(0) 选中 'a'，存入 path[0]，调用 dfs(1)。

        # dfs(1) 选中 'd'，存入 path[1]，调用 dfs(2)。

        # 此时 i = 2，n = 2，触发 i == n：

        # 执行 ''.join(path)，此时 path = ['a', 'd']，生成字符串 "ad"。

        # 执行 ans.append("ad")，将结果保存。
        def dfs(i: int):
            #从0开始回溯
            # n == i break
            if i == n:
                ret1.append(path)
                # print(ret1)
                ret.append(''.join(path))
                return 
            
            for c in MAPPING[int(digits[i])]:
                path[i] = c
                dfs(i+1)

        dfs(0)
        # print(ret1)
        return ret


if __name__ == "__main__":
    s = Solution()
    print(s.letterCombinations("23"))
    print(s.letterCombinations("679"))