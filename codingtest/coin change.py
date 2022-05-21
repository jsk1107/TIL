# -*- coding: utf-8 -*-
# Author: jsk1107
# platform: LeetCode(https://leetcode.com/problems/coin-change/)

"""
    You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
    Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
    You may assume that you have an infinite number of each kind of coin.
"""
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        if dp[-1] == amount + 1:
            dp[-1] = -1
        return dp[-1]

"""
    amount의 값이 나타나게끔 하는 최소 코인의 갯수를 집계하는 문제이다.
    amount=11, coins=[1, 2, 5]일때 F(11)은 [5, 5, 1]로 표현할 수 있다.
    코인5 1개를 빼면 [5, 1]이 되므로 이것은 F(6)이 된다. 즉 F(11)은 F(6) + 1 이 된다. +1은 코인이 된다.(숫자5가 아니라 코인1개를 뜻함)
    코인1 1개를 빼면 [5, 5]이 되므로 이것은 F(10)이 된다. 즉 F(11)은 F(10) + 1 로 표현할 수도 있다.
    F(11)을 만들때 코인2는 포함되지 않지만, F(9)에 코인2를 더하면 11을 만드는 경우의 수도 존재하는것을 알 수 있다.
    
    즉, 이 문제는 F(11)을 만들기 위한 subProblem으로 나타낼 수 있다.
     
    F(11) = F(10) + 1
    F(11) = F(9) + 1   ==> 이중 최소값이 F(11)
    F(11) = F(6) + 1
    -------------------
    F(10) = F(9) + 1
    F(10) = F(8) + 1   ==> 이중 최소값이 F(10)
    F(10) = F(5) + 1
    -------------------
    ...
    -------------------
    F(2) = F(1) + 1
    F(2) = F(0) + 1
    -------------------
    F(1) = F(0) + 1
    -------------------
    
    표를 만들면 아래와 같이 그릴 수 있다
    ---------------------------------------------------------
    |F(0) | F(1) | F(2) | F(3) | F(4) | F(5) | F(6) | F(7) | F(8) | F(9) | F(10) | F(11) |
    |  0  |  1   |  1   |  2   |  2   |  2   |  2   |  2   |  3   |  3   |  3    |  3    |
"""