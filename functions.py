from utils import valida_dados, cria_menssagem, verifica_listas
from utils import calcula_peso_final, varre_lista


def cadastrar_area(area):

    if "nome" not in area:
        nome = input("Insira o nome da area: ")
        area["nome"] = nome

    if "capacidade_max" not in area:
        capacidade = input("Qual é o capacidade maxima da area: ")
        valida_cap = valida_dados(capacidade, False)
        if valida_cap:
            area["capacidade_max"] = capacidade
        else:
            msg = cria_menssagem(
                "Valor inválido. Somente numeros positivos", "valor", "info")
            if msg:
                cadastrar_area(area)
            else:
                print("Cancelando cadastro...")
                return

    if "gmd" not in area:
        gmd = input("Qual é o GMD (Ganho Medio Diario) da area: ")
        valida_gmd = valida_dados(gmd, False)
        print(valida_gmd)
        if valida_gmd:
            area["gmd"] = gmd
            print(
                f"{area['nome']} com o maximo de {area['capacidade_max']} \
animais e GMD de {area['gmd']}")
            print(f"Area {area['nome']} foi cadastrada com sucesso.\n")
        else:
            msg_2 = cria_menssagem(
                "Valor inválido. Somente numeros positivos", "valor", "info")
            if msg_2:
                cadastrar_area(area)
            else:
                print("Cancelando cadastro...")
                return

    return area


def cadastrar_animal(animal):

    if "nome" not in animal:
        brinco = input("Insira o brinco da animal: ")
        animal["nome"] = brinco

    if "peso_inicial" not in animal:
        peso_inicial = input("Qual é o peso inicial do animal: ")
        valida_peso = valida_dados(peso_inicial, False)
        if valida_peso:
            animal["peso_inicial"] = peso_inicial
            print(
                f"Animal {animal['nome']} de peso {animal['peso_inicial']}Kg")
        else:
            msg = cria_menssagem(
                "Valor inválido. Somente numeros positivos", "valor", "info")
            print(msg)
            if msg:
                cadastrar_animal(animal)
            else:
                print("Cancelando cadastro...")
                return
    animal["peso_final"] = 0
    return animal


def movimenta_animais(movimento, lista_areas, lista_animais):

    lista_check = verifica_listas(
        lista_areas, lista_animais, "areas", "animais")
    if lista_check is False:
        return
    else:
        varre_animais = varre_lista(lista_animais, False, "nome")
        print(f"Animais: {varre_animais}")
        animal_input = input("Qual animal voce quer movimentar ? ")
        if animal_input in varre_animais:
            movimento["animal"] = animal_input
        else:
            msg = cria_menssagem("Animal inexistente", "animal", "info")
            if msg:
                movimenta_animais(movimento)
            else:
                print("Cancelando movimento...")
                return
        varre_areas_nome = varre_lista(lista_areas, False, "nome", 1)
        print(f"Areas: {varre_areas_nome}")
        area_input = input("Para qual area esse animal vai ? ")
        if area_input in varre_areas_nome:
            movimento["area"] = area_input
        else:
            msg_2 = cria_menssagem("Area inexistente", "area", "info")
            if msg_2:
                movimenta_animais(movimento)
            else:
                print("Cancelando movimento...")
                return

        dias = input("Por quantos dias o animal vai ficar na area ? ")
        valida_dias = valida_dados(dias, False)
        if valida_dias:
            movimento["dias"] = dias
            varre_area_dict = varre_lista(lista_areas, True, area_input)
            area_gmd = varre_area_dict.get("gmd")

            varre_animal_dict = varre_lista(lista_animais, True, animal_input)
            animal_peso_i = varre_animal_dict.get("peso_inicial")

            varre_animal_dict = varre_lista(lista_animais, True, animal_input)
            animal_peso_f = varre_animal_dict.get("peso_final")

            if animal_peso_f != 0:
                engorda = calcula_peso_final(animal_peso_f, area_gmd, dias)
            else:
                engorda = calcula_peso_final(animal_peso_i, area_gmd, dias)

            print(
                f"Animal {movimento['animal']} foi para {movimento['area']} por\
                {movimento['dias']} dias.\n")
        else:
            msg_3 = cria_menssagem(
                "Valor inválido. Somente numeros positivos", "valor", "info")
            if msg_3:
                movimenta_animais(movimento)
            else:
                print("Cancelando movimento...")
                return

    return engorda, varre_animal_dict


def resultados(lista_animais):
    opcao = input("Voce deseja ver como os resultados:\n\
        1. todos os animais.\n\
        2. animais especificos\n")
    valida_opcao = valida_dados(opcao, True, [1, 2])

    if valida_opcao:
        if opcao == "1":
            varre_tudo = varre_lista(
                lista_animais, False, "nome", "peso_final", 3)
            print(varre_tudo)
        if opcao == "2":
            animais_nomes = varre_lista(lista_animais, False, "nome", 1)
            print(animais_nomes)
            seleciona_animais = input(
                "Quais animais desjea ver os resultados? ")
            nomes_animais = seleciona_animais.split(",")
            nomes_busca = [x for x in nomes_animais]
            for nome in nomes_busca:
                if nome in animais_nomes:
                    pega_dicionarios = varre_lista(
                        lista_animais, False, nome, 3)
                    del(nomes_busca[0])
                    print(pega_dicionarios)

    else:
        msg = cria_menssagem(
            "Opcao invalida, utilize os valores da legenda", "opcao", "info")
        if msg:
            resultados(lista_animais)
        else:
            print("Cancelando resultados...")
            return


def mostrar_opcoes(lista_areas, lista_animais):
    print("\nSelecione o que deseja fazer seguindo a legenda abaixo.")
    opcao = input("\
        1. cadastrar uma area;\n\
        2. cadastrar um animal;\n\
        3. movimentar animais;\n\
        4. ver resultados.\n\
        5. sair.\n")
    if opcao == "1":
        cadastro_area = cadastrar_area({})
        return cadastro_area, "area"
    elif opcao == "2":
        cadastro_animais = cadastrar_animal({})
        return cadastro_animais, "animal"
    elif opcao == "3":
        resultado_movimento = movimenta_animais({}, lista_areas, lista_animais)
        return resultado_movimento
    elif opcao == "4":
        resultados(lista_animais)
    elif opcao == "5":
        msg = cria_menssagem("Voce escolheu sair da aplicao", "sair", "conf")
        if msg:
            print("Saindo da aplicacao...")
            return False
        else:
            mostrar_opcoes(lista_areas, lista_animais)
    else:
        print("Opcao invalida digite um valor de acordo com as legendas.")
        mostrar_opcoes(lista_areas, lista_animais)
