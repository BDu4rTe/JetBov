from functions import mostrar_opcoes


lista_areas = [
    {'nome': 'pasto1', 'capacidade_max': '2', 'gmd': '2'},
    {'nome': 'pasto2', 'capacidade_max': '3', 'gmd': '1'},
]
lista_animais = [
    {'brinco': 'b1', 'peso_inicial': '120', 'peso_final': 0},
    {'brinco': 'b2', 'peso_inicial': '100', 'peso_final': 0},
]


for item in lista_animais:
    for x in item.items():
        print(x)

print("\nSeja bem-vindo ao simulador de Pastejo Rotacionado da JETBOV.")

while True:
    dados = mostrar_opcoes(lista_areas, lista_animais)
    if dados is False:
        break
    if dados is None:
        continue
    temp_bd = [x for x in dados]
    if temp_bd[1] == "area":
        lista_areas.append(temp_bd[0])
    if temp_bd[1] == "animal":
        lista_animais.append(temp_bd[0])
    print(lista_areas)
    print(lista_animais)
