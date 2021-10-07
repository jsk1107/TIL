# -*- coding: utf-8 -*-
# Author: jsk1107
# platform: LeetCode

"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
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
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])

        # binary search
        left, right = 0, m * n - 1
        while left <= right:
            pivot_idx = (left + right) // 2
            pivot_element = matrix[pivot_idx // n][pivot_idx % n]
            if target == pivot_element:
                return True
            else:
                if target < pivot_element:
                    right = pivot_idx - 1
                else:
                    left = pivot_idx + 1
        return False

    def searchMatrix2(self, matrix: List[List[int]], target: int) -> bool:

        row = len(matrix)
        col = len(matrix[0])

        for i in range(row):
            if matrix[i][col - 1] < target:
                continue
            else:
                for j in range(col):
                    if matrix[i][j] == target:
                        return True
                    elif matrix[i][j] < target:
                        continue
                    else:
                        return False


if __name__ == '__main__':
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 3
    solution = Solution()
    output = solution.searchMatrix(matrix, target)
    print(output)

"""
행렬의 값은 왼쪽에서 오른쪽으로 값이 오름차순 정렬된 형태이고, 위에서 아래로 내려갈수록 값이 커진다고 하였다.
가장먼저 해야할 것은, 전체 행렬크기 대비 중앙값을 선별하는것이다. 원소값을 선택하는것이 아님을 유의한다.
해당 예제에서는 pivot_idx를 통해 중앙의 위치가 5라는것을 확인하였다.
MxN 행렬이기 때문에 해당 위치를 Col의 갯수인 N으로 나눈 목과 나머지에 해당하는 위치가 중앙위치의 원소값이 된다.
Row의 갯수인 M을 사용하면 값이 위에서 아래로 정렬된 형태여야 한다.

여기까지 진행했으면 모든 Setting이 끝난것이다.
이진탐색을 통해 Target의 값과 우리가 특정한 원소값을 비교하여 값이 작으면 pivot_idx를 1감소 시켜 right에 할당하여 왼쪽에서 탐색을 다시 시작하고,
크다면 1증가시켜 left에 할당하고 오른쪽에서 탐색을 시작한다.

 while 반복문을 수행하며 target에 해당하는 값이 행렬에 존재하면 True반환하고,
 이진탐색이 끝날때까지 값이 존재하지 않으면 False를 반환하고 종료하게 된다.
"""
