# -*- coding: utf-8 -*-
# Author: jsk1107
# platform: LeetCode(https://leetcode.com/problems/counting-bits/)

"""
    Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n),
    ans[i] is the number of 1's in the binary representation of i.
"""


class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        count = 0

        for i in range(n + 1):
            res.append(self.transform_int2binary(i, count))

        return res

    def transform_int2binary(self, i, count):
        """ return binary """
        if i < 2:
            if i == 1:
                count += 1
            return count

        quotient, mod = divmod(i, 2)
        if mod == 1:
            count += 1

        if quotient == 1:
            count += 1
            return count

        return self.transform_int2binary(quotient, count)

"""
    재귀함수를 통해 문제를 해결하였다(DP 문제는 아닌거 같은...).
    함수의 출력은 2진 변환이 완료된 후, 1의 갯수를 counting하여 return하는 구조이다.
    1. 입력으로 들어온 값이 0,1 두가지의 경우는 if문을 통해 바로 count를 return하도록 한다. 
    2. 3이상의 수가 들어온 경우 10진수를 2진수로 변환하기위해서 divmod 함수를 사용한다.
    3. 나머지(mod)가 1이면 count를 1개 증가시킨다.
    4. 몫이 1이되면 마찬가지로 count를 1개 증가시키고, 더이상 2진수로의 변환이 되지 않는 최종단계이므로 count를 return한다.
    5. 몫이 2 이상이라면 재귀함수를 호출하여 1~4번을 반복한다.
    
    count 변수가 파라미터로 전달되기 때문에, 재귀함수를 호출할 시 count가 계속해서 업데이트 되게된다.
    시간복잡도: O(nlog(n))
        
"""