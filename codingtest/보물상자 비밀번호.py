# -*- coding: utf-8 -*-
# Author: jsk1107
# platform: sw expert academy

import sys

sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    number = input().split()[0]

    length = int(n / 4)
    result_dict = {}
    reference_dict = {}
    for i in range(4):
        n = number[length * i:length * (i + 1)]

        reference_dict[n] = int(n, 16)

    flag = False
    while not flag:
        number = number[-1] + number[:-1]

        for i in range(4):
            n = number[length * i:length * (i + 1)]
            result_dict[n] = int(n, 16)
            if reference_dict.get(n) is not None:
                flag = True
            else:
               flag = False

    li = list(result_dict.values())
    li.sort(reverse=True)
    print(f'#{test_case} {li[k-1]} ')
