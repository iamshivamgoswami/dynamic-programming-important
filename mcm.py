import math


class Solution:
    def matrixMultiplication(self, n, l):
        i = 1
        j = n - 1
        d = {}

        def solve(i, j):

            if i >= j:
                return 0
            if (i, j) in d:
                return d[(i, j)]

            minn = math.inf
            for k in range(i, j):
                temp = solve(i, k) + solve(k + 1, j) + l[i - 1] * l[k] * l[j]
                minn = min(minn, temp)
                d[(i, j)] = minn

            return minn

        return solve(i, j)