from utils import mostra_resultado, valida_dados, cria_menssagem
from utils import calcula_peso_final, varre_lista, verifica_listas


def cadastrar_area(area, lista_areas):
    """
    Faz o cadastro das areas utilizando os inputs do usuario.
    param area : dict
    param lista_areas : list

    Retorna o dict area.\n
    return = {}
    """
    if "nome" not in area:
        nome = input("Insira o nome da area: ")
        area_existe = varre_lista(lista_areas, "nome", 1, nome)
        if area_existe:
            msg = cria_menssagem(
                "Area ja cadastrada.", "inserir um nome diferente")
            if msg:
                cadastrar_area(area, lista_areas)
            else:
                print("Cancelando cadastro...")
                return
        else:
            area["nome"] = nome

    if "capacidade_max" not in area:
        capacidade = input("Qual é o capacidade maxima da area: ")
        valida_cap = valida_dados(capacidade, False)
        if valida_cap:
            area["capacidade_max"] = capacidade
        else:
            msg_i = cria_menssagem(
                "Valor inválido. Somente numeros positivos",
                "inserir um novo valor")
            print(msg_i)
            if msg_i:
                cadastrar_area(area, lista_areas)
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
            msg_3 = cria_menssagem("Valor inválido. Somente numeros positivos",
                                   "inserir um novo valor")
            if msg_3:
                cadastrar_area(area, lista_areas)
            else:
                print("Cancelando cadastro...")
                return

    return area


def cadastrar_animal(animal, lista_animais):
    """
    Faz o cadastro dos animais utilizando os inputs do usuario.
    param animal : dict

    Retorna o dict animal.\n
    return = {}
    """
    if "nome" not in animal:
        brinco = input("Insira o brinco da animal: ")
        animal_existe = varre_lista(lista_animais, "nome", 1, brinco)
        if animal_existe:
            msg = cria_menssagem(
                "Animal ja cadastrado.", "inserir um brinco diferente")
            if msg:
                cadastrar_animal(animal, lista_animais)
            else:
                print("Cancelando cadastro...")
                return
        else:
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
                "Valor inválido. Somente numeros positivos",
                "inserir um novo valor")
            print(msg)
            if msg:
                cadastrar_animal(animal)
            else:
                print("Cancelando cadastro...")
                return
    animal["peso_final"] = 0
    return animal


def movimenta_animais(movimento, lista_areas, lista_animais):
    """
    Faz a movimentacao dos animais.\n
    Pede alguns dados para o usuario e com esses dados
    ela imprime a movimentacao e retorna o peso final do animal e o
    dicionario ao qual ele pertence.
    param movimento : dict
    param lista_areas : list
    param lista_animais : list

    Retorna uma tupla com peso final do animal e o dicionario ao
    qual ele pertence.\n
    return = (int, {})
    """
    lista_check = verifica_listas(
        lista_areas, lista_animais, "areas", "animais")
    if lista_check is False:
        return
    else:
        varre_animais = varre_lista(lista_animais, "nome", 2)
        print(f"Animais: {varre_animais}")
        animal_input = input("Qual animal voce quer movimentar ? ")
        if animal_input in varre_animais:
            movimento["animal"] = animal_input
        else:
            msg = cria_menssagem("Animal inexistente",
                                 "inserir um novo animal")
            if msg:
                movimenta_animais(movimento, lista_areas, lista_animais)
            else:
                print("Cancelando movimento...")
                return
        varre_areas_nome = varre_lista(lista_areas, "nome", 2)
        print(f"Areas: {varre_areas_nome}")
        area_input = input("Para qual area esse animal vai ? ")
        if area_input in varre_areas_nome:
            movimento["area"] = area_input
        else:
            msg_2 = cria_menssagem("Area inexistente",
                                   "inserir uma nova area")
            if msg_2:
                movimenta_animais(movimento, lista_areas, lista_animais)
            else:
                print("Cancelando movimento...")
                return

        dias = input("Por quantos dias o animal vai ficar na area ? ")
        valida_dias = valida_dados(dias, False)
        if valida_dias:
            movimento["dias"] = dias

            varre_area_dict = varre_lista(lista_areas, "nome", 1, area_input)
            print(varre_area_dict)
            area_gmd = varre_area_dict[0].get("gmd")

            varre_animal_dict = varre_lista(
                lista_animais, "nome", 1, animal_input)
            animal_peso_i = varre_animal_dict[0].get("peso_inicial")

            varre_animal_dict = varre_lista(
                lista_animais, "nome", 1, animal_input)
            animal_peso_f = varre_animal_dict[0].get("peso_final")

            if animal_peso_f != 0:
                engorda = calcula_peso_final(animal_peso_f, area_gmd, dias)
            else:
                engorda = calcula_peso_final(animal_peso_i, area_gmd, dias)

            print(
                f"Animal {movimento['animal']} foi para {movimento['area']}\
por {movimento['dias']} dias.\n")
        else:
            msg_3 = cria_menssagem(
                "Valor inválido. Somente numeros positivos",
                "inserir um novo valor")
            if msg_3:
                movimenta_animais(movimento, lista_areas, lista_animais)
            else:
                print("Cancelando movimento...")
                return

    return engorda, varre_animal_dict[0]


def resultados(lista_animais):
    """
    Exibe os resultados do pastejo rotacionado.
    param lista_animais : list
    """
    opcao = input("Voce deseja ver como os resultados:\n\
        1. todos os animais.\n\
        2. animais especificos\n")

    valida_opcao = valida_dados(opcao, True, [1, 2])

    if valida_opcao:
        if opcao == "1":
            varre_tudo = varre_lista(
                lista_animais, "nome", 4, "peso_final")
            mostra_resultado(varre_tudo)
        if opcao == "2":
            animais_nomes = varre_lista(lista_animais, "nome", 2)
            print(animais_nomes)
            seleciona_animais = input(
                "Quais animais deseja ver os resultados? ")
            nomes_animais = seleciona_animais.split(",")
            nomes_busca = [x for x in nomes_animais]
            resultado_busca = []

            for nome in nomes_busca:
                if nome in animais_nomes:
                    pega_dicionarios = varre_lista(
                        lista_animais, "nome", 1, nome)
                    resultado_busca.append(pega_dicionarios)
            for x in resultado_busca:
                v = varre_lista(x, "nome", 4, "peso_final")
                print("#####")
                mostra_resultado(v)

    else:
        msg = cria_menssagem(
            "Opcao invalida, utilize os valores da legenda",
            "inserir uma nova opcao")
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
        cadastro_area = cadastrar_area({}, lista_areas)
        return cadastro_area, "area"
    elif opcao == "2":
        cadastro_animais = cadastrar_animal({}, lista_animais)
        return cadastro_animais, "animal"
    elif opcao == "3":
        resultado_movimento = movimenta_animais({}, lista_areas, lista_animais)
        return resultado_movimento
    elif opcao == "4":
        resultados(lista_animais)
    elif opcao == "5":
        msg = cria_menssagem("Voce escolheu sair da aplicao",
                             "mesmo sair")
        if msg:
            print("Saindo da aplicacao...")
            return False
        else:
            mostrar_opcoes(lista_areas, lista_animais)
    else:
        print("Opcao invalida digite um valor de acordo com as legendas.")
        mostrar_opcoes(lista_areas, lista_animais)
