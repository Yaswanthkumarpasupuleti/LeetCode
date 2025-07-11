# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.root = root
        result = []
        return self.preorder(self.root,result)


    def preorder(self,root,result):
        if not root:
            return []

        result.append(root.val)
        self.preorder(root.left,result)
        self.preorder(root.right,result)
        return result
        