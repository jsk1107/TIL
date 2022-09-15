# -*- coding: utf-8 -*-
# Author: jsk1107
# platform: LeetCode(https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)


from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        pointer_left = 0
        pointer_right = 1
        size = len(prices)
        while pointer_right < size:

            if prices[pointer_left] < prices[pointer_right]:
                res = max(res, prices[pointer_right] - prices[pointer_left])
            else:
                pointer_left = pointer_right
            pointer_right += 1
        return res

"""
   두개의 Pointer를 도입하여 문제를 해결하였다. 처음에는 브루트포스 방식으로 모든 값을 검사하였으나, 시간초과가 발생하고 말았다.
   가장 큰 이익을 내는것은 저점에사서 고점에 파는것이므로,
   
   왼쪽 포인터 < 오른쪽 포인터
   인 경우 오른쪽 포인터를 하나씩 이동시켜서 계산을 진행하면된다. 반대로,
   왼쪽 포인터 > 오른쪽 포인터 
   인 경우 오른쪽 포인터의 값이 작다는 뜻 이므로, 왼쪽 포인터를 오른쪽 포인터의 위치로 변경하여 해당 지점부터 다시 검사하면 된다.
   이렇게 하면 검색속도를 획기적으로 단축시킬 수 있으며, 시간초과가 발생하지 않았다.
"""