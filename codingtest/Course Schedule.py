# -*- coding: utf-8 -*-
# Author: jsk1107
# Platform: Leetcode(https://leetcode.com/problems/course-schedule/)

from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj_list = self.get_adj_list(numCourses, prerequisites)
        visited = [False] * numCourses

        queue = deque([])

        for node in range(numCourses):
            if self.has_cycle_dfs(adj_list, visited, queue, node):
                return False
        return True

    def has_cycle_dfs(self, adj_list, visited, queue, node):
        if visited[node]:
            if node in queue:
                return True
            return False

        visited[node] = True
        queue.append(node)

        for n in adj_list[node]:
            if self.has_cycle_dfs(adj_list, visited, queue, n):
                return True

        queue.pop()
        return False

    def get_adj_list(self, numNode, edge):
        graph = [[] for _ in range(numNode)]
        for e1, e2 in edge:
            graph[e1].append(e2)

        return graph