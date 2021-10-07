# -*- coding: utf-8 -*-
# Author: jsk1107
# platform: 프로그래머스

from collections import deque, defaultdict


def bfs(visited, graph):

    deq = deque()
    deq.append(1)

    while deq:

        node = deq.popleft()

        if visited[node-1][0] == 1:  # 이미 방문 한 노드는 건너뛰기.
            continue
        visited[node-1][0] = 1  # 방문처리.

        edge = graph[node]  # 해당 노드의 간선에 해당하는 노드들.

        check_deq = set(deq)
        for e in edge:
            if visited[e - 1][0] == 1 or e in check_deq:
                continue
            deq.append(e)
            visited[e-1][1] = visited[node-1][1] + 1
    return visited


def create_graph(edge):
    graph = defaultdict(list)
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
    return graph


def solution(n, edge):
    answer = 0
    graph = create_graph(edge)
    visited = [[0, 0] for _ in range(n)] # visit, dist
    visited = bfs(visited, graph)

    max_dist = max(visited)[1]

    for v in visited:
        if v[1] == max_dist:
            answer += 1
    return answer


n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n, vertex))
