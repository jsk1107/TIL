# -*- coding: utf-8 -*-
# Author: jsk1107
# Platform: Leetcode(https://leetcode.com/problems/symmetric-tree/)

from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        queue = deque([(root.left, root.right)])

        while queue:

            l_node, r_node = queue.popleft()

            if l_node is None and r_node is None:
                continue
            if l_node is None or r_node is None or l_node.val != r_node.val:
                return False
            if l_node.val == r_node.val:
                queue.append((l_node.left, r_node.right))
                queue.append((l_node.right, r_node.left))
        return True