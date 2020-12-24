from math import sqrt

X = input().split()
Y = input().split()
x1 = float(X[0])
y1 = float(X[1])
x2 = float(Y[0])
y2 = float(Y[1])
x = x2 - x1
y = y2 - y1
x = pow(x, 2)
y = pow(y, 2)
d = x + y
d = sqrt(d)
print('{:.4f}'.format(d))
