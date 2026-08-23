# 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，
# 满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        tmp = root.val
        # p q 都在左子树
        if p.val < tmp and q.val < tmp:
            return self.lowestCommonAncestor(root.left,p,q)
        # p q 都在右子树
        if p.val > tmp and q.val > tmp:
            return self.lowestCommonAncestor(root.right,p,q)

        # pq在两侧,返回当前节点,或其他
        return root


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