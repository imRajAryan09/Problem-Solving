# 94. Binary Tree Inorder Traversal [https://leetcode.com/problems/binary-tree-inorder-traversal/]
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        st, res = [], []
        cur = root
        while cur or st:
            while cur:
                st.append(cur)
                cur = cur.left
            cur = st.pop()
            res.append(cur.val)
            cur = cur.right
        return res
