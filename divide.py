a = int(input('Digite o número a ser dividido: '))
b = int(input('Digite o divisor: '))
c = 0

while a > 0:
    a -= b
    if a < 0:
        break
    c += 1

print('A divisão é igual a: ', c)