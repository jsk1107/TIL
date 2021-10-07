# -*- coding: utf-8 -*-
# Author: jsk1107
# platform: 프로그래머스

import math

def solution(brown, yellow):
    n1 = math.sqrt(yellow)

    if (n1 % 1) == 0: # 정방형
        return [int(n1 + 2), int(n1 + 2)]
    # 가로가 긴 직사각형
    cnt = 0
    case = []
    while yellow > cnt:
        cnt += 1
        quotient, remainder = divmod(yellow, cnt)
        if remainder != 0:
            continue
        if quotient < cnt:
            continue
        case.append((quotient, cnt))
    for width, height in case:

        width, height = width + 2, height + 2
        if (width * height) - yellow == brown:
            answer = [width, height]
            return answer


brown = 8
yellow = 1
print(solution(brown, yellow))