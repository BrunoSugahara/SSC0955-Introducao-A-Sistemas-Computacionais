import random

memoryArray = []
memorySize = 100
aux = 0
n = 0
p = 0

for i in range(0, memorySize):
    n = random.randint(0, 100)
    memoryArray.append(n)

while aux == 0 or aux == 1:
    aux = int(input('Digite 0 para acessar a memória\nDigite 1 para salvar na memória\nDigite 2 para sair\n'))
    if aux == 0:
        p = int(input('Escolha uma posição de 0 a 99 para acessar: '))
        print('Conteúdo da posição {}: {}\n'.format(p, memoryArray[p]))
    elif aux == 1:
        p = int(input('Escolha uma posição de 0 a 99 para salvar: '))
        n = input('Digite o número a ser salvo: ')
        memoryArray[p] = n
        print('{} salvo na posição {}\n'.format(n, p))
    elif aux == 2:
        break