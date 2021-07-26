
class Solution:
    def palindromicPartition(self, string):
        def ispal(i, j):
            return s[i:j + 1] == s[i:j + 1][::-1]

        d = {}

        def solve(i, j):
            if (i, j) in d:
                return d[(i, j)]

            if i > j:
                d[(i, j)] = 0
                return 0
            if ispal(i, j):
                d[(i, j)] = 0
                return 0
            ans = math.inf
            for k in range(i, j):
                if (i,k) in d:
                    left=d[(i,k)]
                else:
                    left=solve(i,k)

                if (k+1,j) in d:
                    right=d[(k+1,j)]
                else:
                    right=solve(k+1,j)

                ans=min(ans,1+left+right)

                d[(i,j)]=ans
            return d[(i, j)]

        return solve(0, len(s) - 1)

