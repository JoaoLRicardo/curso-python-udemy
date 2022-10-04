import copy
# clientes = {
#     'cliente1' : {
#         'nome' : 'Luiz',
#         'sobrenome' : 'Otávio',
#     },
#     'cliente2' : {
#         'nome' : 'João',
#         'sobrenome' : 'Moreira',
#     },
#     'cliente3' : {
#         'nome' : 'Maria',
#         'sobrenome' : 'Moreira',
#     },
# }

# for cliente_k, clientes_v in clientes.items():
#     print(f'Exibindo {cliente_k}')
#     for dados_k, dados_v in clientes_v.items():
#         print(f'\t{dados_k} = {dados_v}')

# d1 = {1: 'a', 2: 'B', 3: 'C', 'd': ['Luiz', 'Otávio']}
# v = d1.copy()

# v[1] = 'Luiz'
# v['d'][0] = 'Joãozinho'

# print(d1)
# print(v)

# d1 = {1: 'a', 2: 'B', 3: 'C', 'd': ['Luiz', 'Otávio']}
# v = copy.deepcopy(d1)

# v[1] = 'Luiz'
# v['d'][0] = 'Joãozinho'

# print(d1)
# print(v)

d1 = {
    1: 4,
    2: 5,
    3: 6,
}

d2 = {
    'a': 'b',
    'c': 'd',
}
d1.update(d2) # contatenar dois dicionários
d1.pop(3)    # .popitem() elimina sempre o ultimo item.
print(d1)
