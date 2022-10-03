# def func(*args):
#     print(args)


# lista = [1, 2, 3, 4, 5]
# n1, n2, *n = lista
# print(n1, n2, n)
# print('-' * 30)
# print(*lista, sep='**')


# def func(*args):
#     print(args)
#     print(args[0])
#     print(args[-1])
#     print(len(args))


# func(1, 2, 3, 4, 5)


# def func(*args):
#     args = list(args)
#     args[0] = 20
#     print(args)


# func(1, 2, 3, 4, 5)


def func(*args, **kwargs):
    print(args)
    print(kwargs['nome'], kwargs['sobrenome'])
    nome = kwargs.get('nome')
    print(nome)
    idade = kwargs.get('idade')
    if idade is not None:
        print(idade)
    else:
        print('Idade não existe.')      # opcional


lista = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]
func(*lista, *lista2, nome='Luiz', sobrenome = 'Miranda')
