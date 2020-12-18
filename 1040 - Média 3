notas = list(input().split())
n1 = float(notas[0])
n2 = float(notas[1])
n3 = float(notas[2])
n4 = float(notas[3])
media = ((n1*2) + (n2*3) + (n3*4) + (n4*1))/10
print(f'Media: {media:.1f}')
if media >= 7.0:
    print(f'Aluno aprovado.')
elif media < 5.0:
    print(f'Aluno reprovado.')
elif media >= 5.0 and media <= 6.9:
    print(f'Aluno em exame.')
    exame = float(input())
    print(f'Nota do exame: {exame:.1f}')
    nova_media = (exame+media)/2
    if nova_media >= 5.0:
        print(f'Aluno aprovado.')
        print(f'Media final: {nova_media:.1f}')
    else:
        print(f'Aluno reprovado.')
        print(f'Media final: {nova_media:.1f}')
