from math import sqrt
entrada = input().split()
A = float(entrada[0])
B = float(entrada[1])
C = float(entrada[2])

delta = (B*B) - (4*A*C)
try:
    raiz_delta = sqrt(delta)
except:
    print('Impossivel calcular')
else:
    if A == 0 or raiz_delta < 0:
        print('Impossivel calcular')
    else:
        X1 = (-B + raiz_delta) / (2 * A)
        X2 = (-B - raiz_delta) / (2 * A)
        print('R1 = {:.5f}'.format(X1))
        print('R2 = {:.5f}'.format(X2))
