# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
from typing import Optional


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Time-Complexity: O(2n) = O(n). Need to iterate over all the items of p and q
        # Space-Complexity: O(2n) = O(n). Call stack is of height O(n)
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False

    def isSameTree1(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Time-Complexity: O(n). Need to iterate over all the items of p and q
        # Space-Complexity: O(2n) = O(n). Use two queues of length n.
        if not p and not q:
            return True
        queue_p = deque([p])
        queue_q = deque([q])
        while queue_p and queue_q:
            node_p = queue_p.popleft()
            node_q = queue_q.popleft()

            # If both are leaf-nodes, we can continue, to re-enter the while lloop
            if node_p is None and node_q is None:
                continue

            # If only p or q is None, or values don't match, we exit, knowing Trees are not the same
            if node_p is None or node_q is None or node_p.val != node_q.val:
                return False

            queue_p.append(node_p.left)
            queue_p.append(node_p.right)
            queue_q.append(node_q.left)
            queue_q.append(node_q.right)

        return True
