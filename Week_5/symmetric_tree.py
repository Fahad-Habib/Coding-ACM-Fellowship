class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        symmetric = [True]
        def inorder(node1, node2):
            if node1 and node2:
                if node1.val != node2.val:
                    symmetric.append(False)
                inorder(node1.left, node2.right)
                inorder(node1.right, node2.left)
            elif node1 and not node2:
                symmetric.append(False)
            elif node2 and not node1:
                symmetric.append(False)
        inorder(root.left, root.right)
        return False not in symmetric
