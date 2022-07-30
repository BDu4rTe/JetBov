def valida_dados(valor_a_checar, range, valores_validos=[]):

    valido = False
    if valor_a_checar.isnumeric():
        if range:
            valido = int(valor_a_checar) in valores_validos
        elif int(valor_a_checar) > 0:
            valido = True
            return valido

    return valido


def cria_menssagem(msg, tipo):
    resposta = input(
        f"{msg}\nDeseja informar um novo {tipo}? [s] para sim OU [n] para nao.")

    if resposta == "s":
        print("True")
        return True
    elif resposta == "n":
        print("False")
        return False
    else:
        print("Opcao invalida digite um valor de acordo com as legendas.")
        cria_menssagem(msg, tipo)

# direciona_opcao = {
#     1: cadastrar_area(),
#     2: cadastrar_animal(),
#     3: movimenta_animais(),
#     4: engorda()
# }
