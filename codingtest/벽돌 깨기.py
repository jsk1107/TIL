# -*- coding: utf-8 -*-
# Author: jsk1107
# platform: sw expert academy

import sys
from copy import deepcopy


def drop_block(matrix):
    global h, w
    tmp_matrix = [[0 for _ in range(h)] for _ in range(w)]
    remainder_block = 0
    for i in range(h):
        row = w - 1
        for j in range(w - 1, -1, -1):
            v = matrix[j][i]
            if v == 0:
                continue
            tmp_matrix[row][i] = v
            remainder_block += 1
            row -= 1
    return tmp_matrix, remainder_block


def dfs(block_cnt, imple_matrix, row, col):
    global h, w
    if row < 0 or row >= w or col < 0 or col >= h:
        return block_cnt, imple_matrix
    value = imple_matrix[row][col]
    if value != 0:
        imple_matrix[row][col] = 0
        block_cnt += 1
    else:
        return block_cnt, imple_matrix

    for i in range(value-1):
        i+=1
        block_cnt, imple_matrix = dfs(block_cnt, imple_matrix, row+i, col)
        block_cnt, imple_matrix = dfs(block_cnt, imple_matrix, row, col-i)
        block_cnt, imple_matrix = dfs(block_cnt, imple_matrix, row, col+i)
        block_cnt, imple_matrix = dfs(block_cnt, imple_matrix, row-i, col)

    return block_cnt, imple_matrix


def drop_ball(block_cnt_list, n, matrix, imple_cnt):
    global w, h, result_cnt_list, remainder_block_list

    for i in range(h):
        imple_matrix = deepcopy(matrix[imple_cnt])
        row, col = 0, i

        while row < w-1:
            value = imple_matrix[row][col]
            if value == 0:
                row += 1
            else:
                break
        block_cnt, imple_matrix = dfs(0, imple_matrix, row, col)
        imple_matrix, remainder_block = drop_block(imple_matrix)
        matrix.append(imple_matrix)
        block_cnt_list.append(block_cnt)
        imple_cnt += 1
        if imple_cnt != n:
            block_cnt_list, imple_cnt, matrix = drop_ball(block_cnt_list, n, matrix, imple_cnt)
        else:
            result_cnt_list.append(sum(block_cnt_list))
            remainder_block_list.append(remainder_block)
            imple_cnt -= 1
            matrix.pop()
            block_cnt_list.pop()

        if i == h-1:
            imple_cnt -= 1
            matrix.pop()
            block_cnt_list.pop()
    return block_cnt_list, imple_cnt, matrix


sys.stdin = open("input.txt", "r")
T = int(input())

for test_case in range(1, T + 1):
    n, h, w = map(int, input().split())
    matrix = [[list(map(int, input().split())) for _ in range(w)]]
    result_cnt_list = []
    remainder_block_list = []
    block_cnt_list = [0]
    block_cnt = 0
    imple_cnt = 0
    cnt_list, imple_cnt, matrix = drop_ball(block_cnt_list, n, matrix, imple_cnt)

    idx = result_cnt_list.index(max(result_cnt_list))
    print(f'#{test_case} {remainder_block_list[idx]}')









