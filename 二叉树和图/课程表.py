from collections import deque
from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # graph[i]：学完课程 i 后，可以继续学习哪些课程
        # graph[i] 用于存储 pre:i cource:graph[i]
        # 因为一个先修课程可能对应多个后续课程
        graph = [[] for _ in range(numCourses)]

        #indegree[i]:用于记录 课程i 还有多少门先修课程
        indegree = [0] * numCourses


        for cource,pre in prerequisites:
            graph[pre].append(cource)
            indegree[cource] += 1

        # 所有没有先修课程的先入队
        queue = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        ret = 0
        while queue:
            # 弹出最左侧
            tmp = queue.popleft()
            ret += 1

            # 当前课程完成后，
            # 所有依赖它的课程都少一个先修课程
            for tmp_cource in graph[tmp]:
                indegree[tmp_cource] -= 1
                
                # 所有先修课程都完成，可以学习
                if indegree[tmp_cource] == 0:
                    queue.append(tmp_cource)

        return ret == numCourses

if __name__ == "__main__":
    solution = Solution()
    numCourses = 2
    prerequisites = [[1,0]]
    result = solution.canFinish(numCourses, prerequisites)
    print(result)  # 输出: True

    numCourses = 2
    prerequisites = [[1,0],[0,1]]
    result = solution.canFinish(numCourses, prerequisites)
    print(result)  # 输出: False