# -*- coding: utf-8 -*-
# Author: jsk1107
# platform: 프로그래머스
# 풀이날짜: 2021.05.29.
# 소요시간: 2.5시간

from collections import deque


def solution(n, computers):
    answer = 0
    visited = [0 for _ in range(n)]

    deq = deque()

    for idx, node in enumerate(visited):

        if node == 0:

            deq.append(idx)
            bfs(deq, visited, computers)
            answer += 1
    return answer


def bfs(deq, visited, computers):

    while deq:

        node = deq.popleft()
        visited[node] = 9
        edge = computers[node]

        for vertex, e in enumerate(edge):
            if vertex == node:
                computers[node][vertex] = 9
                continue
            if e == 1:
                deq.append(vertex)
                computers[node][vertex] = 9
                computers[vertex][node] = 9


n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(solution(n, computers))