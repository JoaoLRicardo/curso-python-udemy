# add (adiciona), update (atualiza), clear, discard
# union | (une)
# intersection & (todos os elementos presentes nos dois sets)
# difference - (elementos apenas no set da esquerda)
# symmetric_difference ^ (Elementos que estão nos dois sets, mas não em ambos)
# s1 = set()
# s1.add(1)
# s1.add(2)
# s1.add((1, 2, 3, 'Luiz'))
# s1.discard(1)
# print(s1)

# s1 = set()
# s2 = set()
# s1.update([1, 2, 3, 4, 5], {5, 6, 7, 8})     # não aceita elementos duplicados
# s2.update('Python')

# print(s1)
# print(s2)


# l1 = [1, 2, 1, 1, 1, 4, 5, 5, 5, 6, 6, 6, 6, 'Luiz', 'Luiz']
# l1 = set(l1)
# l1 = list(l1)
# print(l1)


# s1 = {1, 2, 3, 4, 5}
# s2 = {1, 2, 3, 4, 5, 6}
# s3 = s1 | s2
# print(s3)
# s3 = s1 & s2
# print(s3)


# s1 = {1, 2, 3, 4, 5, 7}
# s2 = {1, 2, 3, 4, 5, 6}
# s3 = s1 - s2
# print(s3)
# s3 = s1 ^ s2
# print(s3)

# l1 = ['Luiz', 'João', 'Maria']
# l2 = ['Luiz', 'Luiz', 'Luiz', 'João', 'Maria', 'Maria', 'Maria']

# l1 = list(set(l1))
# l2 = list(set(l2))

# print(l1, l2)


l1 = ['Luiz', 'João', 'Maria']
l2 = ['Luiz', 'Luiz', 'Luiz', 'João', 'Maria', 'Maria', 'Maria']

if set(l1) == set(l2):
    print('L1 igual L2')
else:
    print('L1 diferente de L2')
