from typing import Any


def valida_dados(valor_a_checar, range, valores_validos=[]):
    """
    Verifica dados.
    param valor_a_checar : Any
    param range : bool
    param valores_validos : list
    """
    valido = False
    if valor_a_checar.isnumeric():
        if range:
            valido = int(valor_a_checar) in valores_validos
        elif int(valor_a_checar) > 0:
            valido = True
            return valido

    return valido


def cria_menssagem(msg, msg_2):
    """
    Cria mensagens que no final pede uma confirmacao ao usuario.
    param msg : str
    param msg_2 : str\n
    Ela vai dar um print:\n
    {msg}\n
    Deseja {msg_2} ? [s] => sim OU [n] => nao\n
    E vai retornar um bool.
    """
    resposta = input(
        f"{msg}\nDeseja {msg_2}? [s] => sim OU [n] => nao ")
    if resposta == "s":
        print("sim")
        return True
    elif resposta == "n":
        print("nao")
        return False
    else:
        print("Opcao invalida digite um valor de acordo com as legendas.")
        cria_menssagem(msg, msg_2)


def verifica_listas(lista_a, lista_b, tipo_a, tipo_b):
    """
    Verifica se as listas estao vazias.
    param lista_a : list
    param lista_b : list
    param tipo_a : str
    param tipo_b : str\n
    Ela vai da um print:\n
    Voce nao cadastrou {tipo_n} ainda!\n
    E vai retornar um bool.
    """
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
    """
    Calcula o peso final do animal.
    param peso : int
    param gmd : int
    param dias : int

    Ela retorna um int 
    """
    return int(peso) + (int(gmd) * int(dias))


def varre_lista(lista, key, opcao, key_2=None):
    """
    Varre listas de dicionarios para pegar dicionarios ou valores dos mesmos.
    param lista : list
    param key : str
    param opcao : int
    param key_2 : str\n
    Opcoes:\n
    opcao = 1 : pega o dicionario que o valor na chave {key} igual a {key_2}
    \n
    opcao = 2 : pega os valores da chave {key} de cada dicionario na {lsita}\n
    opcao = 3 : imprime os valores das chaves {key} e {key_2} de cada
    dicionario na {lista}\n
    opcao = 4 : pega os calores das chaves {key} e {key_2} de cada
    dicionario na {lista}\n

    Retorna uma lista

    """
    retorno = []
    if opcao == 1:
        for d in lista:
            if d[key] == key_2:
                retorno.append(d)
    if opcao == 2:
        for dicionarios in lista:
            retorno.append(dicionarios[key])
    if opcao == 3:
        for dicionarios in lista:
            print(dicionarios[key], dicionarios[key_2])
    if opcao == 4:
        for d in lista:
            retorno.append(d[key])
            retorno.append(d[key_2])
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
