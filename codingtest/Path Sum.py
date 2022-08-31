# -*- coding: utf-8 -*-
# Author: jsk1107
# Platform: Leetcode(https://leetcode.com/problems/path-sum/)

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

"""
    DFS를 통해 문제를 해결하였다.
    처음에는 Binary Tree를 check하는 함수를 만들었으나, root to leaf는 꼭 Binary Tree가 아니어도 조건을 만족한다는 사실을 알았다.
    
    따라서, dfs 순회를 하면서 left의 leaf 노드까지 진행한다.
    진행하는 과정에서 left, right 노드 양쪽 모두 None인지 체크를 한다. 둘다 None인 경우는 leaf 노드로 간주할 수 있으므로
    targetSum과 값을 비교하여 같으면 True를 return 한다.
    
    만약 한쪽으로만 간선이 나있을 경우, 간선이 없는쪽으로 순회하는경우 무조건 False를 return 하게 되어있기 때문에,
    Binary Tree인지 아닌지를 체크할 필요가 없다.
    
    dfs의 마지막 return을 or 조건으로 묶었기 때문에 한쪽이 True라면 다른쪽은 검사하지 않고 바로 결과를 반환하게 된다.
"""