# -*- coding: utf-8 -*-
# Author: jsk1107
# platform: LeetCode

"""
Given an array nums of n integers where n > 1,
return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Input:  [1,2,3,4]
Output: [24,12,8,6]

Note: Please solve it without division and in O(n).
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
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        result = []

        p = 1
        for i in range(0, len(nums)):
            result.append(p)
            p *= nums[i]

        p = 1
        for i in range(len(nums)-1, 0-1, -1):
            result[i] *= p
            p *= nums[i]

        return result


if __name__ == '__main__':
    input_data = [1, 2, 3, 4]
    solution = Solution()
    output = solution.productExceptSelf(input_data)
    print(output)

"""
해당 문제는 나누기를 할 수 없고 시간복잡도 O(N)이라는 제약조건이 있기 때문에 문제풀이가 상당히 까다롭다.

우선 주어진 배열을 다시 문자로 표기해보면 [a1, a2, a3, a4]로 표시할 수 있다.
최종 결과는 [a2*a3*a4, a1*a3*a4, a1*a2*a4, a1*a2*a3]이 될 수있음을 알 수 있다.

아이디어는 왼쪽에서 곱해나간 결과값을 오른쪽에서 곱해나간 결과값이랑 곱하는것이다. 이게 무슨말이냐면,

가변수 1이라는 숫자를 만든 후 주어진 배열의 왼쪽부터 차례대로 곱해나간다. 그러면 [1, 1*a1, 1*a1*a2, 1*a1*a2*a3] 이된다.
이때 마지막까지 곱한 1*a1*a2*a3*a4는 최종결과에서 나올 수 없는 경우의 수 이므로 a4까지 곱할 필요는 없다.

이제 다시 오른쪽에서부터 곱해나가 생성된 배열을 만들어보면  [a2*a3*a4*1, a3*a4*1, a4*1, 1]이 된다.

이제 왼쪽에서 생성된 배열과 오른쪽에서 곱해나가 생성된 배열 각각의 인덱스끼리 곱해나가면 최종 결과값을 얻을 수 있다는 것이다. 
"""