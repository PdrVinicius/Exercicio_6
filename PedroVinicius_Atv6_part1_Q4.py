def valorGorjeta(valorconta, pagarGorj ,taxa = 0.12):
    if pagarGorj == 'S':
        return valorconta*taxa
    return 0

valid = ('S','N')
tax = None

print('-'*30)
val = float(input('Digite o valor da conta: R$ '))

while not tax in valid:
    tax = input('Você deseja pagar a gorjeta? [S/N] ').upper()

print(f'\nValor da gorjeta é: R$ {valorGorjeta(val,tax)}')
print(f'Valor total da conta é {valorGorjeta(val,tax)+val}')