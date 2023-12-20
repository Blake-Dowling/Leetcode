# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def calc_use(self, node):
        
        if node.left:
            self.calc_use(node.left)
        if node.right:
            self.calc_use(node.right)
        node.val = [node.val, 0]
        if node.left:
            node.val[0] = node.val[0] + node.left.val[1] #use
            node.val[1] = node.val[1] + max(node.left.val[0], node.left.val[1])#dont use
        if node.right:
            node.val[0] = node.val[0] + node.right.val[1] #use
            node.val[1] = node.val[1] + max(node.right.val[0], node.right.val[1])#dont use
        

    def rob(self, root: Optional[TreeNode]) -> int:
        self.calc_use(root)
        return max(root.val[0], root.val[1])