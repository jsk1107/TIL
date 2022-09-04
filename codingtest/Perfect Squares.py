# -*- coding: utf-8 -*-
# Author: jsk1107
# Platform: Leetcode(https://leetcode.com/problems/perfect-squares/)


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

"""
    많은 풀이에서 DP로 접근을 하였으나, 도저히 이해가 안되어서 BFS로 풀이하였다.
    Perfect Square 숫자를 하나씩 꺼내면서, n과의 뺄샘을 진행하다가 0이 등장하는 최초의 순간의 BFS Level을 체크하면 된다.
    
    BFS문제라고해서 반드시 queue 한개를 가지고 pop을 진행하며 검사하지 않아도 된다. for문으로 해결할 수 있다면 그것도 좋다.
    
    핵심 아이디어는 두개의 queue를 가지고 계산한다는 것이다.
    한 Level의 모든 너비를 계산하는것은 이중 For문을 통해 진행한다. queue에 들어있는 값 하나마다 squares을 하나씩 계산해주어야 하기 때문이다.
    계산이 완료된 값은 check_queue에 임시로 넣어준다.
    모든 계산이 끝나면, 해당 Level의 노드를 다시 검사할 수 있도록 queue = check_queue 를 사용한다.
"""