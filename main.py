from functions import mostrar_opcoes, cadastrar_animal, cadastrar_area
from functions import movimenta_animais, engorda


print("\nSeja bem-vindo ao simulador de Pastejo Rotacionado da JETBOV.")
print("----------/----------/----------/----------/----------")

print("Selecione o que deseja fazer seguindo a legenda abaixo.")
bv = mostrar_opcoes()

if bv == "1":
    cadastro_area = cadastrar_area({})
elif bv == "2":
    cadastrar_animal({})
elif bv == "3":
    movimenta_animais()
elif bv == "4":
    engorda()
else:
    print("Opcao invalida digite um valor de acordo com as legendas.")
    mostrar_opcoes()

areas = [cadastro_area]
