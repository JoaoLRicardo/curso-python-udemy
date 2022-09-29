var = ['Luiz Otávio', 'Joãozinho', 'Maria']

for valor in var:
    if valor.lower().startswith('j'):
        continue  # pula para o próximo laço, "Usar o debug para entender"
    print(valor)
