# -*- coding: utf-8 -*-
# Author: jsk1107
# platform: LeetCode(https://leetcode.com/problems/same-tree/)


from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if p is None and q is None:
            return True
        elif p is None and q is not None or p is not None and q is None:
            return False
        else:
            if p.val != q.val:
                return False
            else:
                if self.isSameTree(p.left, q.left):
                    if self.isSameTree(p.right, q.right):
                        return True
                else:
                    return False
