# -*- coding: utf-8 -*-
# Author: jsk1107
# platform: LeetCode

"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.

DO NOT allocate another 2D matrix and do the rotation.

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
"""

import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import *


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)
        m = n
        cnt = 0

        while cnt < m // 2:

            lt, rt, rb, lb = self.matrix_idx(cnt, m)

            for i in range(1, n):
                matrix[rt[0]][rt[1]], matrix[rb[0]][rb[1]], matrix[lb[0]][lb[1]], matrix[lt[0]][lt[1]] = \
                matrix[lt[0]][lt[1]], matrix[rt[0]][rt[1]], matrix[rb[0]][rb[1]], matrix[lb[0]][lb[1]]

                #  n1 = matrix[lt[0]][lt[1]]
                #  n2 = matrix[rt[0]][rt[1]]
                #  n3 = matrix[rb[0]][rb[1]]
                #  n4 = matrix[lb[0]][lb[1]]

                #  matrix[lt[0]][lt[1]] = n4
                #  matrix[rt[0]][rt[1]] = n1
                #  matrix[rb[0]][rb[1]] = n2
                #  matrix[lb[0]][lb[1]] = n3

                lt[1] = lt[1] + 1
                rt[0] = rt[0] + 1
                rb[1] = rb[1] - 1
                lb[0] = lb[0] - 1
            n -= 2
            cnt += 1
        return matrix

    def matrix_idx(self, cnt, n):
        lt = [cnt, cnt]
        rt = [cnt, n - 1 - cnt]
        rb = [n - 1 - cnt, n - 1 - cnt]
        lb = [n - 1 - cnt, cnt]

        return lt, rt, rb, lb


if __name__ == '__main__':
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    solution = Solution()
    output = solution.rotate(matrix)
    print(output)

"""

"""
