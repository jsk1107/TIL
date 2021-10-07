# -*- coding: utf-8 -*-
# Author: jsk1107
# platform: LeetCode

"""
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]
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
    def generateMatrix(self, n: int) -> List[List[int]]:

        if not n:
            return []

        res = [[0 for _ in range(n)] for _ in range(n)]

        top, right, bottom, left = 0, n - 1, n - 1, 0
        num = 1

        while num <= n ** 2:

            if top == right:
                mid = n // 2
                res[mid][mid] = num
                return res

            for i in range(left, right):
                res[top][i] = num
                num += 1

            for i in range(top, bottom):
                res[i][right] = num
                num += 1

            for i in range(right, left, -1):
                res[bottom][i] = num
                num += 1
            for i in range(bottom, top, -1):
                res[i][left] = num
                num += 1

            top += 1
            right -= 1
            bottom -= 1
            left += 1

        return res


if __name__ == '__main__':
    n = 5
    solution = Solution()
    output = solution.generateMatrix(n)
    print(output)

"""
가장 먼저 입력된 숫자크기만큼의 row, col을 가진 2D-Array에 0을 채워넣는 작업을 수행했다.
그리고 해당 List의 좌상단부터 시계방향으로 돌아가면서 값을 하나씩 채워나갈 수 있도록 구성하였다.
채워나가는 값은 상,하,좌,우 모두 움직이기 때문에 이것을 가리킬 수 있는 Index를 top, right, bottom, left 로 지정하였다.
시작 위치가 좌상단이므로 top=0, left=0이고 right=n-1, bottom=n-1로 가장 마지막 위치로 초기화 한다.

채워나갈 숫자를 num=1로 지정하고 while 반복문을 통해 작업을 수행한다.

for 반복문통해 왼쪽에서 오른쪽으로 index를 이동시키면서 가장 위쪽 껍질에 값을 채워나간다. 
반복문이 종료된 후, 위에서 아래로 index를 이동시키면서 가장 오른쪽 껍질에 값을 채워나간다. 
이제 오른쪽에서 왼쪽으로 index를 이동시키면서 맨 아래쪽 껍질에 값을 채워나간다. 
마지막으로 아래에서 위쪽으로 index를 이동시키면서 왼쪽 껍질에 값을 채워나간다.


이렇게 while 반복문을 1회 수행하면 가장 바깥쪽 값이 모두 채워지게 된다.
다음으로 안쪽 껍질을 채워나가기 위해 top, left는 1씩 증가시키고 right, bottom은 1씩 감소시켜 index를 조정한다.
이때 고려해야할 사항이 하나 있다. 3x3, 5x5, ... 와 같은 정방행렬의 경우에는 값을 채워나가는 과정에서 중앙에 값이 1개 남아버리게된다. 
이러한 경우를 고려하여 마지막에 수행될 수 있도록 while 반복문의 맨 위에 if 조건문을 하나 추가해주었다.
"""
