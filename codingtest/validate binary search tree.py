# -*- coding: utf-8 -*-
# Author: jsk1107
# platform: LeetCode(https://leetcode.com/problems/validate-binary-search-tree/)


from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = []
        self.inOrder(root, res)
        return res == sorted(res) and len(set(res)) == len(res)

    #         for i in range(1, len(res)):

    #             if res[i-1] < res[i]:
    #                 continue
    #             else:
    #                 return False
    #         return True

    def inOrder(self, root, res):
        if root is None:
            return

        self.inOrder(root.left, res)
        res.append(root.val)
        self.inOrder(root.right, res)