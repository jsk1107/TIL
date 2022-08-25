# -*- coding: utf-8 -*-
# Author: jsk1107
# platform: LeetCode(https://leetcode.com/problems/binary-tree-inorder-traversal/)


from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def depth_check(root, depth):

            if not root:
                return depth
            else:
                left_depth = depth_check(root.left, depth+1)
                right_depth = depth_check(root.right, depth+1)

                return max(left_depth, right_depth)

        return depth_check(root, 0)


"""
    dfs로 해결하였다. 새로운 메서드를 만들어서 Node와 depth를 파라미터로 받을 수 있게 한다.
    Node를 넣었을때 None이 들어있다면 해당 depth를 return해준다.
    
    만약 None이 아니라면 왼쪽 노드를 계속 순회한다. 이때 depth는 메서드 내부에서 값을 변경하지 않는다.
    Left 순회가 다 끝나고 return이 된 depth를 left_depth에 받는다.
    그리고 다시 Right 순회를 시작한다. 마찬가지로 순회가 끝난 후 return 된 depth를 right_depth에 받는다.
    
    이 두가지 값중 큰 값(max)의 depth가 가장 깊은 depth가 된다. leaf Node에서 left, right depth는 무조건 똑같지만,
    root Node에서 left, right depth는 다르기 때문 
    
    계산되는 순서는 아래와 같다.
    maxDepth(9): max(2,2)=2
    maxDepth(15): max(3,3)=3
    maxDepth(7): max(3,3)=3
    maxDepth(20): max(3,3)=3 <- left value는 maxDepth(15)의 값, right value는 maxDepth(7)의 값
    maxDepth(3): max(2,3)=3 <- left value는 maxDepth(9)의값, right value는 maxDepth(20)의 값
"""