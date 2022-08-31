# -*- coding: utf-8 -*-
# Author: jsk1107
# Platform: Leetcode(https://leetcode.com/problems/symmetric-tree/)

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        if root is None:
            return False

        total_sum = 0
        return self.dfs(root, total_sum, targetSum)

    def dfs(self, root, total_sum, targetSum):
        if root is None:
            return False

        total_sum += root.val

        if root.left is None and root.right is None and total_sum == targetSum:
            return True

        return self.dfs(root.left, total_sum, targetSum) or self.dfs(root.right, total_sum, targetSum)