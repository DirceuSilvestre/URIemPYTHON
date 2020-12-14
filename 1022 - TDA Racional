from math import gcd
x = int(input())
N1 = list()
N2 = list()
D1 = list()
D2 = list()

NP = list()
DP = list()
NNP = list()
DDP = list()
for x in range(0, x):
    v = input().split()
    N1.append(int(v[0]))
    D1.append(int(v[2]))
    N2.append(int(v[4]))
    D2.append(int(v[6]))
    if v[3] == '+':
        NP.append(N1[x]*D2[x] + N2[x]*D1[x])
        DP.append(D1[x]*D2[x])
    elif v[3] == '-':
        NP.append(N1[x]*D2[x] - N2[x]*D1[x])
        DP.append(D1[x]*D2[x])
    elif v[3] == '*':
        NP.append(N1[x] * N2[x])
        DP.append(D1[x]*D2[x])
    else:
        NP.append(N1[x]*D2[x])
        DP.append(N2[x]*D1[x])
    y = gcd(NP[x], DP[x])
    if y == 0:
        NNP.append(NP[x])
        DDP.append(DP[x])
    else:
        NNP.append(NP[x]//y)
        DDP.append(DP[x]//y)
for x in range(0, x+1):
    print('{}/{} = {}/{}'.format(NP[x], DP[x], NNP[x], DDP[x]))
