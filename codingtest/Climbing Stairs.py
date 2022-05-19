# -*- coding: utf-8 -*-
# Author: jsk1107
# platform: LeetCode

"""
    You are climbing a staircase. It takes n steps to reach the top.
    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""


class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 1:
            return 1
        elif n == 2:
            return 2

        result = [1, 2]

        for i in range(n - 2):
            result[0], result[1] = result[1], sum(result)

        return result[1]


"""
    n=1~4까지만 손으로 경우의수를 따져보면 피보나치수열을 이루고 있음을 알 수 있다.
    ## f(n) = f(n-1) + f(n-2)
    
    n=1, 2일때는 조건문을 걸어서 바로 return할 수 있게한다(속도 향상).
    List를 만들고 내부에는 n=1일때 경우의수 1, n=2일때 경우의수 2를 넣어둔다.
    n=3일때는 List의 두 수를 더하면되고,
    n=4일때는 1번 인덱스의 값이 0번인덱스로 교체되고, 두개의 값을 더하여 1번인덱스를 만들어준다.
    n=5일때는 위의 작업을 두번 반복하기면 하면된다. 
    최종 경우의 수는 1번 인덱스의 값을 꺼내서 리턴해준다.
"""