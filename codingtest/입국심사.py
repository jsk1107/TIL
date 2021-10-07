# -*- coding: utf-8 -*-
# Author: jsk1107
# platform: 프로그래머스

def solution(n, times):
    answer = 0

    right = min(times) * n
    left = 1

    while left <= right:

        mid = (left + right) // 2
        remainder = n
        for t in times:
            remainder -= (mid // t)

            if remainder <= 0:
                right = mid - 1
                answer = mid
                break

        if remainder > 0:
            left = mid + 1

    return answer

n = 6
times = [7, 10]
print(solution(n, times))