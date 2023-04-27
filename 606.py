class Solution:
    def tree2str(self, root: TreeNode) -> str:
        if not root:
            return ""
        left = "({})".format(self.tree2str(root.left)) if root.left or root.right else ""
        right = "({})".format(self.tree2str(root.right)) if root.right else ""
        return "{}{}{}".format(root.val, left, right)
