def valida_dados(valor_a_checar, range, valores_validos=[]):

    valido = False
    if valor_a_checar.isnumeric():
        if range:
            valido = int(valor_a_checar) in valores_validos
        elif int(valor_a_checar) > 0:
            valido = True
            return valido

    return valido


def cria_menssagem(msg, info, tipo):
    if tipo == "info":
        resposta = input(
            f"{msg}\nDeseja informar um(a) novo {info}? [s] => sim OU [n] => nao ")
    if tipo == "conf":
        resposta = input(
            f"{msg}\nDeseja mesmo {info}? [s] para sim OU [n] para nao ")
    if resposta == "s":
        return True
    elif resposta == "n":
        return False
    else:
        print("Opcao invalida digite um valor de acordo com as legendas.")
        cria_menssagem(msg, info, tipo)


def verifica_listas(lista_a, lista_b, tipo_a, tipo_b):
    if len(lista_a) == 0 and len(lista_b) == 0:
        print("Voce nao cadastrou nada ainda!")
        return False
    if len(lista_a) == 0:
        print(f"Voce nao cadastrou {tipo_a} ainda!")
        return False
    if len(lista_b) == 0:
        print(f"Voce nao cadastrou {tipo_b} ainda!")
        return False
    else:
        return True


def calcula_peso_final(peso, gmd, dias):
    return int(peso) + (int(gmd) * int(dias))


def varre_lista(lista, bool, key, key_2=None, quantidade=None):
    retorno = []
    if bool:
        for d in lista:
            if d['nome'] == key:
                print(d)
                return d
    if quantidade == 1:
        for dicionarios in lista:
            retorno.append(dicionarios[key])
    if quantidade == 2:
        for dicionarios in lista:
            print(dicionarios[key], dicionarios[key_2])
    return retorno

# def salva_dados(dados, tipo):
#     animais = []
#     areas = []
#     if tipo == "area":
#         areas.append(dados)
#         print(areas)
#         return areas
#     if tipo == "animal":
#         animais.append(dados)
#         return animais

# direciona_opcao = {
#     1: cadastrar_area(),
#     2: cadastrar_animal(),
#     3: movimenta_animais(),
#     4: engorda()
# }
