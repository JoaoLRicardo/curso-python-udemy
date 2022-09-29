#!/usr/bin/env python

"""
Listas em Python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""
secreto = 'aviao'
digitadas = []
chances = 5

while True:
    if chances <= 0:
        print('\033[31mVocê perdeu!!!\033[m')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Ahhh isso não vale, digite apenas uma letra.')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'\033[32mUHUULLL, a letra "{letra}" existe na palavra secreta.\033[m')
    else:
        print(f'\033[31mAFFFzzz: a letra "{letra}" NÃO EXISTE na palavra secreta.\033[m')
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(f'\033[32mQue legal, VOCÊ GANHOU!!! A palavra era {secreto_temporario}.\033[m')
        break
    else:
        print(f'A palavra secreta está assim: \033[33m{secreto_temporario}\033[m')

    if letra not in secreto:
        chances -= 1

    if chances >= 4:
        print(f'\033[32mVocê ainda tem {chances} chances.\033[m')
    elif chances >= 2:
        print(f'\033[33mVocê ainda tem {chances} chances.\033[m')
    else:
        print(f'\033[31mVocê ainda tem {chances} chances.\033[m')
    print()
