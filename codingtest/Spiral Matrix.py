# -*- coding: utf-8 -*-
# Author: jsk1107
# platform: LeetCode

"""
Given an m x n matrix, return all elements of the matrix in spiral order.

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
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
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []

        while matrix:
            result += matrix.pop(0)

            if matrix and matrix[0]:
                for row in matrix:
                    result.append(row.pop())

            if matrix:
                result += matrix.pop()[::-1]

            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    result.append(row.pop(0))

        return result


if __name__ == '__main__':
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    solution = Solution()
    output = solution.spiralOrder(matrix)
    print(output)

"""
result = [1, 2, 3, 4] matrix = [[5, 6, 7, 8], [9, 10, 11, 12]]
result = [1, 2, 3, 4, 8, 12] matrix = [[5, 6, 7], [9, 10, 11]]
result = [1, 2, 3, 4, 8, 12, 11, 10, 9], matrix = [[5, 6, 7]]
result = [1, 2, 3, 4, 8, 12, 11, 10, 9, 5], matrix = [[6, 7]]
result = [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7], matrix = []
"""
