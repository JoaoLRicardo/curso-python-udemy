# def ola_mundo():
#     return 'Olá Mundo!'


# def mestre(funcao):
#     return funcao()


# print(mestre(ola_mundo))


def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


def fala_oi(nome):
    return f'Oi {nome}'


def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'


executando = mestre(fala_oi, 'Luiz')
print(executando)
executando2 = mestre(saudacao, 'Luiz', saudacao='Bom dia!')
print(executando2)
