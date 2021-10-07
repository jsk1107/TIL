# -*- coding: utf-8 -*-
# Author: jsk1107
# platform: 프로그래머스


def solution(progresses, speeds):
    answer = []
    stack = []

    num = len(speeds)
    cnt = 0
    while True:
        progresses = [v1 + v2 for v1, v2 in zip(progresses, speeds)]
        while cnt < num:
            if progresses[cnt] >= 100:
                stack.append(progresses[cnt])
                cnt += 1
            else:
                break

        if stack:
            answer.append(len(stack))
            for _ in range(len(stack)):
                stack.pop()
        if num == cnt:
            break
    return answer


progresses = [93, 30, 55]
speeds = [1, 30, 5]
print(solution(progresses, speeds))