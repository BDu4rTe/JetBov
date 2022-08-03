from functions import mostrar_opcoes
"""
Bem pra comecar o programa se divide em 3 arquivos: main, functions
e utils.

Na main temos o script que roda todo o programa, onde tem os "bancos de dados"
(que nesse caso eu usei listas) e o unico import da main é a mostrar_opcoes,
que é o que gerencia todas as outras funcoes do programa.

No arquivo functions temos as funcoes principais do programa, que vao fazer o
cadastro e manejo de tudo que entrar de dados no programa.

No arquivo utils temos funcoes pequenas que eu criei simplesmente para por em
pratica o DRY e encurtar codigo, sao funcoes simples para tarefas que eu
precisava fazer dentro das funcoes maiores.

As listas depois de preenchidas vao ficar assim:

lista_areas = [
    {'nome': 'pasto1', 'capacidade_max': '10', 'gmd': '2'},
]
lista_animais = [
    {'nome': 'b1', 'peso_inicial': '100', 'peso_final': 0},
]

"""

lista_areas = []
lista_animais = []

if __name__ == "__main__":

    print("\nSeja bem-vindo ao simulador de Pastejo Rotacionado da JETBOV.")

    while True:
        dados = mostrar_opcoes(lista_areas, lista_animais)
        if dados is False:
            break
        if dados == "Cancela":
            print("Cadastro cancelado!")
            continue
        if dados == "Resultado":
            continue
        if dados is None:
            print("\nOcorreu algum erro!!\nPor favor repita a acao.")
            dados = mostrar_opcoes(lista_areas, lista_animais)
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
