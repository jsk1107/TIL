# -*- coding: utf-8 -*-
# Author: jsk1107
# platform: LeetCode

"""
Write an efficient algorithm that searches for a target value in an m x n integer matrix. The matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.

Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true

Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
Output: false
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
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m, n = len(matrix), len(matrix[0])

        pivot_row, pivot_col = 0, n - 1

        while pivot_row < m and pivot_col >= 0:
            if matrix[pivot_row][pivot_col] < target:
                pivot_row += 1
            elif matrix[pivot_row][pivot_col] > target:
                pivot_col -= 1
            else:
                return True
        return False


if __name__ == '__main__':
    matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24],
              [18, 21, 23, 26, 30]]
    target = 35
    solution = Solution()
    output = solution.searchMatrix(matrix, target)
    print(output)

"""

"""
