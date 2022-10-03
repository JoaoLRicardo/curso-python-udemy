
lista = [
    ['P1', 13],
    ['P2', 7],
    ['P3', 20],
    ['P4', 19],
    ['P5', 50]
]

# lista.sort(key=lambda item: item[1], reverse=True)
print(sorted(lista, key=lambda i: i[1], reverse=True))
