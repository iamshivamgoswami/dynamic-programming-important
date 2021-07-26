import sys


def isOperator(op):
    return (op == '+' or op == '*' or op == "-" or op == "/")
def printval(exp):
    num=[]
    opr=[]
    tmp=""
    for i in range(len(exp)):
        if isOperator(exp[i]):
            opr.append(exp[i])
            num.append(int(tmp))
            tmp=""
        else:
            tmp+=exp[i]
    num.append(int(tmp))
    llen = len(num)
    minval = [[0 for i in range(llen)] for i in range(llen)]
    maxval = [[0 for i in range(llen)] for i in range(llen)]
    for i in range(llen):
        for j in range(llen):
            minval[i][j] = sys.maxsize
            maxval[i][j] = -sys.maxsize

            if i == j:
                minval[i][j] = maxval[i][j] = num[i]
    n = len(num)
    for l in range(1, n+1):
        for i in range(n - l+1):
            j = i + l-1
            for k in range(i, j):

                if opr[k] == "+":
                    a = minval[i][k] + maxval[k + 1][j]
                    b = minval[i][k] + minval[k + 1][j]
                    c = maxval[i][k] + minval[k + 1][j]
                    d = maxval[i][k] + maxval[k + 1][j]
                    minval[i][j] = min(minval[i][j], a, b, c, d)
                    maxval[i][j] = max(maxval[i][j], a, b, c, d)
                if opr[k] == "/":
                    a = minval[i][k] / maxval[k + 1][j]
                    b = minval[i][k] / minval[k + 1][j]
                    c = maxval[i][k] / minval[k + 1][j]
                    d = maxval[i][k] / maxval[k + 1][j]
                    minval[i][j] = min(minval[i][j], a, b, c, d)
                    maxval[i][j] = max(maxval[i][j], a, b, c, d)
                if opr[k] == "-":
                    a = minval[i][k] - maxval[k + 1][j]
                    b = minval[i][k] - minval[k + 1][j]
                    c = maxval[i][k] - minval[k + 1][j]
                    d = maxval[i][k] - maxval[k + 1][j]
                    minval[i][j] = min(minval[i][j], a, b, c, d)
                    maxval[i][j] = max(maxval[i][j], a, b, c, d)
                if opr[k] == "*":
                    a = minval[i][k] * maxval[k + 1][j]
                    b = minval[i][k] * minval[k + 1][j]
                    c = maxval[i][k] * minval[k + 1][j]
                    d = maxval[i][k] * maxval[k + 1][j]
                    minval[i][j] = min(minval[i][j], a, b, c, d)
                    maxval[i][j] = max(maxval[i][j], a, b, c, d)
    print(num)
    print(opr)
    return maxval[0][llen - 1]


expr=input()
print(printval(expr))



