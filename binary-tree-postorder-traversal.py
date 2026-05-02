# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.store = []
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def postorder(root):
            if not root:
                return []
            if root.left:
                self.postorderTraversal(root.left)
            if root.right:
                self.postorderTraversal(root.right)
            self.store.append(root.val)
        postorder(root)
        return self.store
