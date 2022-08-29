# -*- coding: utf-8 -*-
# Author: jsk1107
# Platform: Leetcode(https://leetcode.com/problems/symmetric-tree/)

from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        queue = deque([(root.left, root.right)])

        while queue:

            l_node, r_node = queue.popleft()

            if l_node is None and r_node is None:
                continue
            if l_node is None or r_node is None or l_node.val != r_node.val:
                return False
            if l_node.val == r_node.val:
                queue.append((l_node.left, r_node.right))
                queue.append((l_node.right, r_node.left))
        return True

"""
    BFS로 문제를 풀이한다. queue를 하나 생성하고, 하나씩 쌓아나간다.
    이때 중요한것은 symmetric을 동시에 비교해야하기 때문에, 2개의 노드를 Tuple로 묶어서 queue에 넣는것이다.
    그래야 pop()을 실행할때 2개의 노드가 한번에 나오게되기 때문이다.
    
    만약 left 노드와 right 노드의 값이 같으면,
    left노드의 left노드와 right노드의 right노드를 tuple로 묶어서 queue에 넣는다.
    마찬가지로, left노드의 right노드와 right노드의 left노드를 tuple로 묶어서 queue에 넣는다.
    
    만약 leaf Node까지 순회하여 더이상 노드가 없는경우 None이 되므로, 양쪽의 노드를 비교한다.
    둘다 None이면 symmetric이므로 다음 queue를 꺼내기위해 conitnue처리한다.
    
    만약 한쪽 노드에서 가지가 더 뻗어나간경우 None이 아니고, 양쪽 노드의 값이 다른경우 symmetric이 아니므로
    return을 반환하고 while문을 바로 탈출한다.
    
    만약 queue가 모두 빌때까지 순회가 완료되면 symmetric이므로 True를 반환한다. 
"""