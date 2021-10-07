# -*- coding: utf-8 -*-
# Author: jsk1107
# platform: LeetCode

"""
Given an integer array nums of 2n integers,
group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn)
such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.

Input: nums = [6,2,6,5,1,2]
Output: 9
Explanation: The optimal pairing is (2, 1), (2, 5), (6, 6). min(2, 1) + min(2, 5) + min(6, 6) = 1 + 2 + 6 = 9.
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
    def arrayPairSum(self, nums: List[int]) -> int:

        nums.sort()
        return sum(nums[::2])


if __name__ == '__main__':
    input_data = [1, 4, 3, 2]

    solution = Solution()
    output = solution.arrayPairSum(input_data)
    print(output)

"""
알고리즘의 시작은 "정렬"부터가 시작이라고 해도 과언이 아닌것 같다.
무작정 주어진 값에 대해서 탐색과정을 진행하기 전에 정렬을 하면 쉽게 풀릴수 있는지 고민을 하고 시작해보도록 하자.

우선, 2개의 쌍을 이루었을때 최소값의 합이 최대가 되어야한다. 잘 생각해보면 입력받은 배열을 정렬하기만 하면 쉬운문제로 바뀐다.
[1,4,3,2]를 오름차순으로 정렬하면 [1,2,3,4]가 된다. 이제 앞에서부터 순서대로 2개씩 뽑아 쌍을 이루면, 최소값의 합이 최대값이 된다.
min(1,2) + min(3,4) = 1+3 = 4 이런식이다.

min() 함수를 적용하지 않고 다른방법으로 푸는 또하나의 방법은 nums[::2] 슬라이싱 방법을 이용하는 방법이다.
[::2] 라고하는 표현은 0, 2, 4, ... 짝수번째 인덱스를 추출하여 묶어준다. 즉 [1, 3] 이 묶여서 나온다.
이것을 그냥 더하기만 하면 페어들의 최소값의 합이 최대가 된다. 
"""