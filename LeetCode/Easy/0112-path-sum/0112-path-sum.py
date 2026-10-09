# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        if root == targetSum:
            return True
        return self.helper(root, 0, targetSum)

    def helper(self,node,sum, targetSum):
        if node is None:
            return False
        sum+= node.val

        if node.left is None and node.right is None:
            return sum == targetSum

        east = self.helper(node.left, sum, targetSum)
        west = self.helper(node.right,sum, targetSum)
        return east or west