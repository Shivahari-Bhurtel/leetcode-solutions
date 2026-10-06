# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        return self.traverse(nums, 0, len(nums)-1)
    def traverse(self,nums,st_index, end_index):
        if st_index > end_index:
            return None
        mid = st_index + (end_index - st_index)//2
        root = TreeNode(nums[mid])
        root.left = self.traverse(nums,st_index,mid-1)
        root.right = self.traverse(nums,mid+1,end_index)
        return root

            