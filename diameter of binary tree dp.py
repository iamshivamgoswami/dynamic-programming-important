class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        res = 0

        def solve(node, ):
            nonlocal res
            if not node:
                return 0

            if node:
                left = solve(node.left)
                right = solve(node.right)
                temp = max(left, right) + 1
                ans = max(temp, left + right + 1)
                res = max(ans, res)
            return temp

        solve(root)

        return res - 1
