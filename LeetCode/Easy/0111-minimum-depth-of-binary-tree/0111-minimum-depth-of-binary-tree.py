# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode | None) -> int:
        if root is None:
            return 0
        return self.eastwest(root)

    def eastwest(self, node):
        if node is None:
            return 0
        left = self.eastwest(node.left)
        right = self.eastwest(node.right)
        if left == 0:
            return 1 + right
        if right == 0:
            return 1 + left
        return 1+min(left, right)