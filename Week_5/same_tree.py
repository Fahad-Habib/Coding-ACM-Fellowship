class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        same = [True]
        def inorder(node1, node2):
            if node1 and node2:
                inorder(node1.left, node2.left)
                if node1.val != node2.val:
                    same.append(False)
                inorder(node1.right, node2.right)
            elif node1 and not node2:
                same.append(False)
            elif node2 and not node1:
                same.append(False)
        inorder(p, q)
        return False not in same
