# -*- coding: utf-8 -*-
# Author: jsk1107
# platform: LeetCode(https://leetcode.com/problems/validate-binary-search-tree/)


from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = []
        self.inOrder(root, res)
        return res == sorted(res) and len(set(res)) == len(res)

    #         for i in range(1, len(res)):

    #             if res[i-1] < res[i]:
    #                 continue
    #             else:
    #                 return False
    #         return True

    def inOrder(self, root, res):
        if root is None:
            return

        self.inOrder(root.left, res)
        res.append(root.val)
        self.inOrder(root.right, res)

"""
    binary search tree는 중위순회를 할 경우 오름차순 정렬된다는 특징을 가지고 있다.
    따라서 dfs를 통해 중위순회를 모두 진행한다. 그 결과를 list에 담아둔다.
    
    해당 list를 sorted 메서드로 정렬을 했을 때, 같으면 True를 반환하게한다.
    또한, 잊지 말아야 할것이 [2, 2, 2]와 같은 Node가 주어졌을경우는 순회 이후에도 [2, 2, 2]가 된다.
    중복을 제거시킬 수 있도록 set 함수를 사용하여 전체 길이를 비교하여 True, False를 반환한다.
    
    return은 위 두가지 경우를 and 연산자로 묶어 둘다 True일 경우에만 True를 리턴하도록 한다.
"""