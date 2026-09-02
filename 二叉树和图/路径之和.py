from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # DFS 前序遍历 中左右
        if not root:
            return False

        # 叶节点判断
        if not root.left and not root.right:
            return targetSum == root.val
        
        # 非叶子节点，继续向下
        return self.hasPathSum(root.left,targetSum-root.val) or \
        self.hasPathSum(root.right,targetSum-root.val)
        
if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.right.right = TreeNode(1)

    s = Solution()
    print(s.hasPathSum(root, 22))  # 输出: True

    print(s.hasPathSum(root, 26))  # 输出: True