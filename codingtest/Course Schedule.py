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

"""
    처음에는 bfs로 접근했으나, 풀이방법이 직관적이지 못해 dfs로 풀이하였다.
    인접리스트, 방문체크리스트를 만드는것은 기본이다. 
    
    핵심 아이디어는 다음과 같다.
    1. 0번 Node부터 시작해서 n번 노드까지 +1씩 순서대로 순회
    2. edge가 연결된 정점들을 dfs순회 하면서 하나의 queue에 적재됨.
       3 -> 1 -> 4, 3 -> 2 -> 4, 0 -> 5
       이러한 graph라면, [3, 1, 4] 가 하나의 집합으로 queue가 활용된다. 따라서 이 순회가 끝나면 queue는 비어있어야 한다.     
    3. queue의 처리는 LIFO방식으로 진행한다. FIFO라면 가장 먼저 들어온 Node가 pop되기 때문에 cycle 검증이 불가능하다.
    4. visited 변수 Type을 Set으로 하면 좀 더 빠르다. 하지만 직관성을 위해서 List로 풀이하였다.
    5. 방문여부에 대한 검증은 메서드 진입 시점에 확인한다.
    6. 간선이 나가는 방향일때는 방문처리를 하면서 queue에 적재가 된다. 간선이 들어오는 방향일때도 검증을 해야하는데,
       이때 queue에 node가 들어있다면 cycle이 존재하는것이다.
       만약 node가 없다면 [[], [4], [4], [1], []] 이런 케이스이다(1->4 node는 검증이 끝났으나, 3->1 node는 나중에 검증이 시작됨).         
"""