from utils import valida_dados, cria_menssagem, verifica_listas, calcula_peso_final


def cadastrar_area(area):

    if "nome" not in area:
        nome = input("Insira o nome da area: ")
        area["nome"] = nome

    if "capacidade_max" not in area:
        capacidade = input("Qual é o capacidade maxima da area: ")
        valida_1 = valida_dados(capacidade, False)
        if valida_1:
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
        valida_2 = valida_dados(gmd, False)
        print(valida_2)
        if valida_2:
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

    if "brinco" not in animal:
        brinco = input("Insira o brinco da animal: ")
        animal["brinco"] = brinco

    if "peso_inicial" not in animal:
        peso_inicial = input("Qual é o peso inicial do animal: ")
        valida_1 = valida_dados(peso_inicial, False)
        if valida_1:
            animal["peso_inicial"] = peso_inicial
            print(
                f"Animal {animal['brinco']} de peso {animal['peso_inicial']}Kg")
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
        print(lista_animais)
        varre = varrer_lista(lista_animais, "brinco")
        animal_input = input("Qual animal voce quer movimentar ? ")
        if animal_input in varre:
            movimento["animal"] = animal_input
        else:
            msg = cria_menssagem("Animal inexistente", "animal", "info")
            if msg:
                movimenta_animais(movimento)
            else:
                print("Cancelando movimento...")
                return
        for area in lista_areas:
            print(f"Areas: {area['nome']}")
            area_input = input("Para qual esse animal vai ? ")
            if area_input in area["nome"]:
                movimento["area"] = area_input
            else:
                msg_2 = cria_menssagem("Area inexistente", "area", "info")
                if msg_2:
                    movimenta_animais(movimento)
                else:
                    print("Cancelando movimento...")
                    return

        dias = input("Por quantos dias o animal vai ficar na area ? ")
        valida_1 = valida_dados(dias, False)
        if valida_1:
            movimento["dias"] = dias
            engorda = calcula_peso_final(animal, area, dias)
            animal["peso_final"] = engorda
            print(animal)
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
    return


def resultados():
    return "engorda"


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
        movimento = movimenta_animais({}, lista_areas, lista_animais)
        return movimento
    elif opcao == "4":
        resultados()
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
