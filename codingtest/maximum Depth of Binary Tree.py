# -*- coding: utf-8 -*-
# Author: jsk1107
# platform: LeetCode(https://leetcode.com/problems/binary-tree-inorder-traversal/)


from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def depth_check(root, depth):

            if not root:
                return depth
            else:
                left_depth = depth_check(root.left, depth+1)
                right_depth = depth_check(root.right, depth+1)

                return max(left_depth, right_depth)

        return depth_check(root, 0)