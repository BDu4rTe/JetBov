from functions import mostrar_opcoes


lista_areas = [
    {'nome': 'pasto1', 'capacidade_max': '10', 'gmd': '2'},
    {'nome': 'pasto2', 'capacidade_max': '10', 'gmd': '1'},
]
lista_animais = [
    {'nome': 'b1', 'peso_inicial': '100', 'peso_final': 0},
    {'nome': 'b2', 'peso_inicial': '100', 'peso_final': 0},
    {'nome': 'b3', 'peso_inicial': '100', 'peso_final': 0},
    {'nome': 'b4', 'peso_inicial': '100', 'peso_final': 0},
    {'nome': 'b5', 'peso_inicial': '100', 'peso_final': 0},
    {'nome': 'b6', 'peso_inicial': '100', 'peso_final': 0},
]
if __name__ == "__main__":

    print("\nSeja bem-vindo ao simulador de Pastejo Rotacionado da JETBOV.")

    while True:
        dados = mostrar_opcoes(lista_areas, lista_animais)
        if dados is False:
            break
        if dados is None:
            continue
        if None in dados:
            continue
        print(dados)
        temp_bd = [x for x in dados]
        if temp_bd[1] == "area":
            lista_areas.append(temp_bd[0])
        elif temp_bd[1] == "animal":
            lista_animais.append(temp_bd[0])
        else:
            nome = dados[1].get("nome")
            for animal in lista_animais:
                if animal["nome"] == nome:
                    animal["peso_final"] = dados[0]
        print(lista_areas)
        print(lista_animais)
