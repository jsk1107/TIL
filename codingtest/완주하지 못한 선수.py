# -*- coding: utf-8 -*-
# Author: jsk1107
# platform: 프로그래머스


def solution(participant, completion):
    answer = ''

    completion = {p: p for p in completion}
    print(participant)
    for i in range(len(participant)):
        comp = completion.get(participant[i])
        print(participant)
        if comp is None:
            answer = comp
    return answer

participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]

print(solution(participant, completion))