# texto = 'Python'
# for letra in texto:
#     print(f'{letra}')


texto = 'Python'
nova_string = ''

# continue - pula para o proximo laço
# break - termina o laço

for letra in texto:
    if letra == 't':
        # continue  # exemplo de continue "Python ficará PyHon"
        nova_string += letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
        # break  # exemplo de breack "Python ficará PyTH"
    else:
        nova_string += letra

print(nova_string)
