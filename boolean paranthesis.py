import functools


class Solution:
    def countWays(self, n, s):

        @functools.lru_cache(None)
        def solve(i, j, t):


            if i > j:
                return 0
            if i == j:
                if t == True:
                    return 1 if s[i] == "T" else 0
                else:
                    return 1 if s[i] == "F" else 0
            ans = 0

            for k in range(i + 1, j, 2):

                lt = solve(i, k - 1, True)
                lf = solve(i, k - 1, False)

                rt = solve(k + 1, j, True)
                rf = solve(k + 1, j, False)

                if s[k] == "&":

                    if t == True:
                        ans += lt * rt

                    else:
                        ans += lt * rf + lf * rt + lf * rf
                if s[k] == "|":
                    if t == True:
                        ans += lt * rt + lf * rt + lt * rf
                    else:
                        ans += lf * rf
                if s[k] == "^":
                    if t == True:
                        ans += lt * rf + lf * rt
                    else:
                        ans += lt * rt + rf * lf

            return ans

        return solve(0, n - 1, True) % 1003