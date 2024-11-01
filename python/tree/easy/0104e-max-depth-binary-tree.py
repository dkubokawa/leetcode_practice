import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Recursive Depth First Search
        Time: O(N)
        Space: O(1)
        """
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def maxDepth1(self, root: Optional[TreeNode]) -> int:
        """
        Iterative Breadth First Search. i.e. Level order Traversal
        Time: O(N)
        Space: O(1)
        """
        if not root:
            return 0
        level = 0
        q = collections.deque([root])
        while q:
            # traverse the current level (i.e. everything in the queue)
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level


    def maxDepth2(self, root: Optional[TreeNode]) -> int:
        """
        Iterative Depth First Search using Pre-Order (Left) Traversal
        Time: O(N)
        Space: O(1)
        """
        stack = [[root, 1]]
        res = 0
        while stack:
            node, depth = stack.pop()
            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return res
