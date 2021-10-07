# -*- coding: utf-8 -*-
# Author: jsk1107
# platform: LeetCode

"""
Given an m x n matrix. If an element is 0, set its entire row and column to 0. Do it in-place.

Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
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
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        m, n = len(matrix), len(matrix[0])
        zero_col = []
        inp = False

        for i in range(m):
            if 0 in matrix[i]:
                index = [idx for idx, value in enumerate(matrix[i]) if value == 0]
                zero_col.extend(index)
                matrix[i] = [0] * n
                inp = True

        if not inp:
            return matrix

        zero_col = list(set(zero_col))
        for i in zero_col:
            for j in range(m):
                matrix[j][i] = 0
        return matrix


if __name__ == '__main__':
    matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    solution = Solution()
    output = solution.setZeroes(matrix)
    print(output)

"""

"""
