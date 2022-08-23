# -*- coding: utf-8 -*-
# Author: jsk1107
# platform: sw expert academy
# 풀이날짜: 2022.08.16.
# 소요시간: 2.5시간


import sys


def check_name(len_name):
    global samsung

    i = 0
    res = []
    while i <= 7-len_name:

        extract_name = samsung[i: i+len_name]
        res.append(extract_name)

        i+=1
    return res

def dfs(src, cnt):
    global samsung


    len_name, name, score = src['len'][cnt], src['name'][cnt], src['score'][cnt]
    candidate_name = check_name(len_name)
    if name in candidate_name:
        dfs(src, cnt+1)
    else:
        return



DATA_PATH = 'C:\\Users\\QQQ\\Downloads\\sample_input_1.txt'
sys.stdin = open(DATA_PATH, "r")

T = int(input())
for test_case in range(1, T + 1):
    samsung = "SAMSUNG"
    num_person = int(input())

    src = {'len': [], 'name': [], 'score': []}
    for i in range(0, num_person):
        len_name = int(input())
        name = input().replace(' ', '')
        score = int(input())

        src['len'].append(len_name)
        src['name'].append(name)
        src['score'].append(score)

    cnt = 0
    while True:
        dfs(src, cnt)
        cnt += 1



