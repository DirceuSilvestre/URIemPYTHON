entrada = input().split()
A = int(entrada[0])
B = int(entrada[1])
C = int(entrada[2])
D = int(entrada[3])
contador = 0
if B > C and D > A:
    contador += 1
if (C+D) > (A+B):
    contador += 1
if C and D > 0:
    contador += 1
if (A%2) == 0:
    contador += 1

if contador == 4:
    print('Valores aceitos')
else:
    print('Valores nao aceitos')
