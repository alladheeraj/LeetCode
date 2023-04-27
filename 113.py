
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if not root:
            return []       
        def dfs(node, targetSum, path, res):
            if not node:
                return           
            if not node.left and not node.right:
                if targetSum == node.val:
                    res.append(path + [node.val])
                return            
            dfs(node.left, targetSum - node.val, path + [node.val], res)
            dfs(node.right, targetSum - node.val, path + [node.val], res)
        res = []
        dfs(root, targetSum, [], res)
        return res
