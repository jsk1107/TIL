# -*- coding: utf-8 -*-
# Author: jsk1107
# platform: 프로그래머스
# 풀이날짜: 2021.05.29.
# 소요시간: 1시간

from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_deq = deque(truck_weights)
    cross_deq = deque()
    cross_deq.append([0, bridge_length])

    while cross_deq:

        if cross_deq[0][1] == bridge_length:
            cross_deq.popleft()
        for i in cross_deq:
            i[1] += 1

        try:
            if sum(i[0] for i in cross_deq) + truck_deq[0] <= weight:
                truck_weight = truck_deq.popleft()
                cross_deq.append([truck_weight, 1])
        except:
            pass
        answer += 1
    return answer


bridge_length = 100
weight = 100
truck_weights = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
solution(bridge_length, weight, truck_weights)