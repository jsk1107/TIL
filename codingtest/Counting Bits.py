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

        result, mod = divmod(i, 2)
        if mod == 1:
            count += 1

        if result == 1:
            count += 1
            return count

        return self.transform_int2binary(result, count)

