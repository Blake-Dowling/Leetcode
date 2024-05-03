# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        centerIndex = int((len(nums) - 1 ) / 2)
        center = nums[centerIndex]
        left = self.sortedArrayToBST(nums[:centerIndex])
        right = self.sortedArrayToBST(nums[centerIndex+1:])
        return TreeNode(center, left, right)

