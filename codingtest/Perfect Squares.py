# -*- coding: utf-8 -*-
# Author: jsk1107
# Platform: Leetcode(https://leetcode.com/problems/path-sum/)


from collections import deque


class Solution:
    def numSquares(self, n: int) -> int:

        squares = self.get_squares(n)

        level = 0
        queue = deque([n])

        while queue:
            check_queue = deque([])
            level += 1

            for q in queue:
                for square in squares:
                    if square == q:
                        return level
                    if square > q:
                        break
                    check_queue.append(q - square)
            queue = check_queue
        return level

    def get_squares(self, n):
        squares = []
        i = 1
        while i ** 2 <= n:
            squares.append(i ** 2)
            i += 1


        return squares