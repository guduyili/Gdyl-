from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        # 遍历过的1变为7
        def dfs(i,j) -> int:
            # 先判断是否越界再次变化数字
            if i<0 or i >=m or j<0 or j>=n  or grid[i][j] != '1':
                return
            #按照左右上下递归
            # if grid[i][j] == "1":
            grid[i][j] = '7'
            dfs(i,j-1)
            dfs(i,j+1)
            dfs(i-1,j)
            dfs(i+1,j)

        

        ret = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i,j)
                    ret +=1 
        return ret



if __name__ == "__main__":
    s = Solution()
    print(s.numIslands([["1","1","1","1","0"],
                         ["1","1","0","1","0"],
                         ["1","1","0","0","0"],
                         ["0","0","0","0","0"]]))
    print(s.numIslands([["1","1","0","0","0"],
                         ["1","1","0","0","0"],
                         ["0","0","1","0","0"],
                         ["0","0","0","1","1"]]))