class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        traversal = []
        def inorder(node):
            if node:
                inorder(node.left)
                traversal.append(node.val)
                inorder(node.right)
        inorder(root)
        return traversal
