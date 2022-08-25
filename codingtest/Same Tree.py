# -*- coding: utf-8 -*-
# Author: jsk1107
# platform: LeetCode(https://leetcode.com/problems/same-tree/)


from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if p is None and q is None:
            return True
        elif p is None and q is not None or p is not None and q is None:
            return False
        else:
            if p.val != q.val:
                return False
            else:
                if self.isSameTree(p.left, q.left):
                    if self.isSameTree(p.right, q.right):
                        return True
                else:
                    return False


"""
    DFS를 활용하였다. 중요포인트는 return값이 boolean으로 되어있다는것이다.
    
    1.양쪽 Node가 모두 비어있으면 동일depth의 트리이므로 True를 반환한다.
    2.만약 Node의 depth가 달라서, 한쪽 Node는 비어있고 한쪽 Node는 값이 들어있다면 같은 트리가 아니므로 False를 반환한다.
    3.위 두가지 조건이 아니면 순회를 진행한다. 순회는 전위순회를 진행한다. 현재 순회하는 Node의 값을 체크하고 다르면 False를 반환한다.
    4.만약 True라면 left Node를 순회한다. 여기에서 만약 True를 반환한다면(즉, Same left Node) right Node를 순회한다. 
    5.right Node에서도 True를 반환한다면(즉, Same right Node), True를 반환한다.
    6.그렇지 않은경우는 Same Tree라고 할 수 없으므로 False를 반환한다.
"""