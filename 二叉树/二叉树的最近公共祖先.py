class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 如果找到p 或 q 就不会向下递归
        if root in (None,q,p):
            return root
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)

        # 如果左右都有 return root
        if left and right:
            return root
        
        # 有左返左
        # 有右返右
        # 都无返回 None
        return left or right
    

if __name__ == '__main__':
    s = Solution()
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)

    p = root.left  # Node with value 5
    q = root.right  # Node with value 1
    lca = s.lowestCommonAncestor(root, p, q)
    print(lca.val)  # Output should be 3