# -*- coding: utf-8 -*-
# Author: jsk1107
# platform: LeetCode

"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
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
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        result = []

        for i in range(len(nums) - 2):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:

                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
        return result


if __name__ == '__main__':
    input_data = [-2, -1, -1, -1, 0, 0, 0, 1, 1, 1, 2]

    solution = Solution()
    output = solution.threeSum(input_data)
    print(output)

"""
투포인터를 활용한 리스트 탐색 및 비교문제

리스트에서 i번째 인덱스를 고정한 후, 해당 인덱스를 제외한 나머지 리스트에서 첫번째, 마지막번째 인덱스를 셋팅한다.
그리고 첫번째, 마지막 인덱스를 가리키는 포인터를 오른쪽으로, 왼쪽으로 이동시키면서 리스트를 순회한다.

포인터가 가리키는 값을 하나씩 뽑아서 초기에 고정시켜놨던 i번째 인덱스와 더한 합이 0인경우 result에 append시킨다.
세 수의 합이 0일때, 주어진 데이터에 중복되는 값들이 존재할 수 있으므로 (ex. [-2, -1, -1, 0, 1, 1, 4], -1, 1이 중복) 이러한 케이스는
Skip해야한다. while 반복문을 돌면서 left, right 포인터를 이동시켜준다.

while문이 끝난 후에는 마지막으로 포인터를 하나씩 더 움직여준다.
예를들어 [-2, -1, -1, -1, 0, 0, 0, 1, 1, 2, 2]같은 문제가 있을경우 i=0 이었을때, 값은 -2이다.
left 포인터는 1번째 인덱스부터 오른쪽으로 진행하다가 4번째 인덱스에서 값을 뽑게되고, right 포인터는 10번째 인덱스 값을 뽑는다.
다음으로 4번째 인덱스에서 있던 left 포인터가 5번째 인덱스와 값이 같다면 스킵해야하므로 5,6번째 인덱스까지 이동하고 멈춘다.
이제 right 포인터는 왼쪽으로 이동하면서 9번째 인덱스에서 멈춘다.
이제 포인터는 6번째 9번째 인덱스를 가리키고 있다.
맨 마지막에서 포인터를 한번 더 이동시키지 않는다면 sum이 다시 0이되어 else문으로 빠지게되고 
이때, 7번째 8번째 인덱스의 값은 6번째 9번째 인덱스와 값이 같지 않으므로 while문으로 진입을 못하게되고 다시 전체 while문으로 돌아가게 된다. 
이것이 반복하게되어 무한루프에 빠지게 된다.
"""