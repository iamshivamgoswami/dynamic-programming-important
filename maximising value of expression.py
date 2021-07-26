
import sys


# Utility method to check whether a character
# is operator or not
def isOperator(op):
    return (op == '+' or op == '*' or op == "-" or op == "/")


# method prints minimum and maximum value
# obtainable from an expression
def printMinAndMaxValueOfExp(exp):
    num = []
    opr = []
    tmp = ""

    # store operator and numbers in different vectors
    for i in range(len(exp)):
        if (isOperator(exp[i])):
            opr.append(exp[i])
            num.append(int(tmp))
            tmp = ""
        else:
            tmp += exp[i]

            # storing last number in vector
    num.append(int(tmp))

    llen = len(num)
    minval = [[0 for i in range(llen)] for i in range(llen)]
    maxval = [[0 for i in range(llen)] for i in range(llen)]

"""Use dynamic programming method to find the maximum 
possible value for the given arithmetic expression by adding parenthese
5-8+7*4-8+9
op=200"""
    # initializing minval and maxval 2D array
    for i in range(llen):
        for j in range(llen):
            minval[i][j] = sys.maxsize
            maxval[i][j] = -sys.maxsize

            # initializing main diagonal by num values
            if (i == j):
                minval[i][j] = maxval[i][j] = num[i]

                # looping similar to matrix chain multiplication
    # and updating both 2D arrays
    n = len(num)
    for L in range(1, n):
        for i in range(llen - L):
            j = i + L
            for k in range(i, j):

                minTmp = 0
                maxTmp = 0

                # if current operator is '+', updating tmp
                # variable by addition
                if opr[k] == "+":
                    a = maxval[i][k] + maxval[k + 1][j]
                    b = maxval[i][k] + minval[k + 1][j]
                    c = minval[i][k] + maxval[k + 1][j]
                    d = minval[i][k] + minval[k + 1][j]
                    minval[i][j] = min(minval[i][j], a, b, c, d)
                    maxval[i][j] = max(maxval[i][j], a, b, c, d)
                if opr[k] == "-":
                    a = maxval[i][k] - maxval[k + 1][j]
                    b = maxval[i][k] - minval[k + 1][j]
                    c = minval[i][k] - maxval[k + 1][j]
                    d = minval[i][k] - minval[k + 1][j]
                    minval[i][j] = min(minval[i][j], a, b, c, d)
                    maxval[i][j] = max(maxval[i][j], a, b, c, d)
                if opr[k] == "*":
                    a = maxval[i][k] * maxval[k + 1][j]
                    b = maxval[i][k] * minval[k + 1][j]
                    c = minval[i][k] * maxval[k + 1][j]
                    d = minval[i][k] * minval[k + 1][j]
                    minval[i][j] = min(minval[i][j], a, b, c, d)
                    maxval[i][j] = max(maxval[i][j], a, b, c, d)
                if opr[k] == "/":
                    a = maxval[i][k] / maxval[k + 1][j]
                    b = maxval[i][k] / minval[k + 1][j]
                    c = minval[i][k] / maxval[k + 1][j]
                    d = minval[i][k] / minval[k + 1][j]
                    minval[i][j] = min(minval[i][j], a, b, c, d)
                    maxval[i][j] = max(maxval[i][j], a, b, c, d)

                    # updating array values by tmp variables

    # last element of first row will store the result
    return (maxval[0][llen - 1])


# Driver code
expression = input()
print(printMinAndMaxValueOfExp(expression))