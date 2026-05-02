# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = []
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.preorder(root)
        return self.res
    def preorder(self, root):
        if not root:
            return []
        self.res.append(root.val)
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)
