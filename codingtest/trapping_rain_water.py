# -*- coding: utf-8 -*-
# Author: jsk1107
# platform: LeetCode

"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
In this case, 6 units of rain water (blue section) are being trapped.
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
    def trap(self, height: List[int]) -> int:

        stack = []
        vol = 0

        for i in range(len(height)):

            while stack and height[i] > height[stack[-1]]:

                bf_bar_height = stack.pop()

                if not len(stack): break;

                dist = i - 1 - stack[-1]
                water = min(height[i], height[stack[-1]]) - height[bf_bar_height]

                vol += dist * water
            stack.append(i)

        return vol


if __name__ == '__main__':
    input_data = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

    solution = Solution()
    output = solution.trap(input_data)
    print(output)