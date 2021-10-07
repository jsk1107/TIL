# -*- coding: utf-8 -*-
# Author: jsk1107
# platform: LeetCode

"""
Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
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
    def numIslands(self, grid: List[List[str]]) -> int:

        island = 0
        if not grid:
            return island

        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if grid[i][j] == '1':
                    island += 1
                    self.dfs(grid, i, j)
        return island

    def dfs(self, grid, row, col):

        # row, col이 grid의 크기를 벗어나는 경우 return. -> 모든 방향을 순회했다고 봐도 무방하기 때문.
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] != '1':
            return

        grid[row][col] = '#'
        self.dfs(grid, row+1, col) # 아래
        self.dfs(grid, row, col+1) # 오른쪽
        self.dfs(grid, row-1, col) # 왼쪽
        self.dfs(grid, row, col-1) # 위쪽


if __name__ == '__main__':
    input_data = [['1', '1', '1', '1', '0'],
                  ['1', '0', '1', '1', '0'],
                  ['1', '1', '1', '0', '0'],
                  ['0', '0', '0', '1', '0']]

    solution = Solution()
    output = solution.numIslands(input_data)
    print(output)

"""
DFS의 순서는 아래와 같이 진행된다.

[['#', '1', '1', '1', '0'],
 ['1', '0', '1', '1', '0'],
 ['1', '1', '1', '0', '0'],
 ['0', '0', '0', '1', '0']]

[['#', '1', '1', '1', '0'],
 ['#', '0', '1', '1', '0'],
 ['1', '1', '1', '0', '0'],
 ['0', '0', '0', '1', '0']]

[['#', '1', '1', '1', '0'],
 ['#', '0', '1', '1', '0'],
 ['#', '1', '1', '0', '0'],
 ['0', '0', '0', '1', '0']]

[['#', '1', '1', '1', '0'],
 ['#', '0', '1', '1', '0'],
 ['#', '#', '1', '0', '0'],
 ['0', '0', '0', '1', '0']]
 
[['#', '1', '1', '1', '0'],
 ['#', '0', '1', '1', '0'],
 ['#', '#', '#', '0', '0'],
 ['0', '0', '0', '1', '0']]

[['#', '1', '1', '1', '0'],
 ['#', '0', '#', '1', '0'],
 ['#', '#', '#', '0', '0'],
 ['0', '0', '0', '1', '0']]

[['#', '1', '1', '1', '0'],
 ['#', '0', '#', '#', '0'],
 ['#', '#', '#', '0', '0'],
 ['0', '0', '0', '1', '0']]

[['#', '1', '1', '#', '0'],
 ['#', '0', '#', '#', '0'],
 ['#', '#', '#', '0', '0'],
 ['0', '0', '0', '1', '0']]

[['#', '1', '#', '#', '0'],
 ['#', '0', '#', '#', '0'],
 ['#', '#', '#', '0', '0'],
 ['0', '0', '0', '1', '0']]

[['#', '#', '#', '#', '0'],
 ['#', '0', '#', '#', '0'],
 ['#', '#', '#', '0', '0'],
 ['0', '0', '0', '1', '0']]

[['#', '#', '#', '#', '0'],
 ['#', '0', '#', '#', '0'],
 ['#', '#', '#', '0', '0'],
 ['0', '0', '0', '#', '0']]
"""