# -*- coding: utf-8 -*-
# Author: jsk1107
# platform: 프로그래머스

def solution(board, moves):
    answer = 0
    n = len(board)
    stack = []

    for move in moves:
        cnt = 0

        while cnt < n:
            doll = board[cnt][move-1]
            if doll == 0:
                cnt += 1
            else:
                stack.append(doll)
                board[cnt][move-1] = 0
                break

        while True:
            if len(stack) <= 1:
                break

            if stack[-1] != stack[-2]:
                break

            if stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
                answer += 2
    return answer


board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board, moves))
