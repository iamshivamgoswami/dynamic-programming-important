


class Solution:
    def longestCommonSubsequence(self, a: str, b: str) -> int:

        d={}
        def lcs(x,y):
            if (x,y) in d:
                return d[(x,y)]
            if x==0 or y==0:
                d[(x, y)]=0
                return 0
            if a[x-1]==b[y-1]:
                d[(x, y)]=1+lcs(x-1,y-1)
                return d[(x, y)]
            else:
                d[(x, y)]=max(lcs(x,y-1),lcs(x-1,y))
                return d[(x, y)]

        return lcs(len(a),len(b))
