D = input().split()
A = float(D[0])
B = float(D[1])
C = float(D[2])
TRI = (A * C)/2
CIR = (C*C)*3.14159
TRA = ((A + B) * C)/2
QUA = B * B
RET = A * B
print('''TRIANGULO: {:.3f}
CIRCULO: {:.3f}
TRAPEZIO: {:.3f}
QUADRADO: {:.3f}
RETANGULO: {:.3f}'''.format(TRI, CIR, TRA, QUA, RET))
