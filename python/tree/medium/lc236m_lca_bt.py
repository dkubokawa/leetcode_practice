# LC 236 (Medium): Lowest Common Ancestor of a Binary Tree

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if p == q:
            return p
        if root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # search the left of the tree for P or Q (whichever is higher)
        # if left = val and right = None, then top-most left is the LCA
        # if right = None and right = val, then top-most right is the LCA
        # if left = val and right = val, root is the LCA
        if left is not None and right is not None:
            return root
        if left:
            return left
        if right:
            return right