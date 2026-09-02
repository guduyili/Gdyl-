# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return 0
            # 后序遍历 左右中
            left = dfs(root.left)
            if left == -1: return -1
            right = dfs(root.right)
            if right == -1: return -1
            return max(left,right) + 1 if abs(left-right) <=1 else -1

        # tmp = dfs(root)
        # if tmp == -1:
        #     return False
        # return True
        return dfs(root) != -1


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(3)
    root.left.left.left = TreeNode(4)
    root.left.left.right = TreeNode(4)

    s = Solution()
    print(s.isBalanced(root))  # 输出: False


    # 
    print(s.isBalanced(TreeNode(1)))  # 输出: True
    
                