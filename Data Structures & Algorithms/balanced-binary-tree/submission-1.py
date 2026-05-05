# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        def dfs(root):
            if not root:
                return 0
            leftH = dfs(root.left)
            rightH = dfs(root.right)

            if abs(leftH - rightH) > 1:
                self.balanced = False

            return 1 + max(leftH, rightH)
        dfs(root)
        return self.balanced


            