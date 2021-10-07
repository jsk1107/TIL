# -*- coding: utf-8 -*-
# Author: jsk1107
# platform: LeetCode

"""
Given a positive integer num, write a function which returns True if num is a perfect square else False.
Follow up: Do not use any built-in library function such as sqrt.

Input: num = 16
Output: true

Input: num = 14
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
    def isPerfectSquare(self, num: int) -> bool:

        if num == 1:
            return True

        left = 0
        right = num

        while left + 1 != right:

            mid = (left + right) // 2

            if mid ** 2 > num:
                right = mid
            elif mid ** 2 < num:
                left = mid
            else:
                return True
        return False


if __name__ == '__main__':
    num = 16
    solution = Solution()
    output = solution.isPerfectSquare(num)
    print(output)

