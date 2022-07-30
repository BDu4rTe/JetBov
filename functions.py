from utils import valida_dados, cria_menssagem


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
                "Valor inválido. Somente numeros positivos", "valor")
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
                "Valor inválido. Somente numeros positivos", "valor")
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
        else:
            msg = cria_menssagem(
                "Valor inválido. Somente numeros positivos", "valor")
            if msg:
                cadastrar_animal(animal)
            else:
                print("Cancelando cadastro...")
                return

    return animal


def movimenta_animais(movimento, animais, areas):

    animal = input("Qual animal voce quer movimentar ? ")
    if animal in animais:
        movimento["animal"] = animal
    else:
        msg = cria_menssagem("Animal inexistente", "animal")
        if msg:
            movimenta_animais(movimento)
        else:
            print("Cancelando movimento...")
            return

    area = input("Para qual esse animal vai ? ")
    if area in areas:
        movimento["area"] = area
    else:
        msg_2 = cria_menssagem("Area inexistente", "area")
        if msg_2:
            movimenta_animais(movimento)
        else:
            print("Cancelando movimento...")
            return

    dias = input("Por quantos dias o animal vai ficar na area ? ")
    valida_1 = valida_dados(dias, False)
    if valida_1:
        movimento["dias"] = dias
        print(
            f"Animal {movimento['animal']} foi para {movimento['area']} por\
            {movimento['dias']} dias.\n")
    else:
        msg_3 = cria_menssagem(
            "Valor inválido. Somente numeros positivos", "valor")
        if msg_3:
            movimenta_animais(movimento)
        else:
            print("Cancelando movimento...")
            return

    return movimento


def engorda():
    return "engorda"


def mostrar_opcoes():
    opcao = input("\
        1. cadastrar uma area;\n\
        2. cadastrar um animal;\n\
        3. movimentar animais;\n\
        4. ver resultados.\n")
    return opcao
