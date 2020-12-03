def contagem(i, f, p):
    print('-='*10)
    print(f'Contagem de {i} até {f} passo {p}')
    for num in range(i, f, p):
        print(num, end=' ')
    print('FIM')


contagem(1, 10, 1)
contagem(10, 0, 2)

print('Personalize sua Contagem:')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contagem(inicio, fim, passo)