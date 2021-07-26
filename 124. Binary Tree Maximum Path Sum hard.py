import math


class Solution:
    def maxPathSum(self, root):
        res = -math.inf

        def solve(node):
            nonlocal res
            if not node:
                return 0
            left = solve(node.left)
            right = solve(node.right)

            temp = max(max(left, right) + node.val, node.val)
            ans = max(temp, left + right + node.val)
            res = max(res, ans)
            return temp

        solve(root)
        return res





