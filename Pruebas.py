nombres = ""
lista_nombres = []

for i in range(100):
    menu = input("Seleccione una opcion:\n 1- Ingrese Dato:\n 2- Imprimir lista: \n 3- Salir")
    if menu == "1":
        lista_nombres.append(nombres)
        nombres = input("Ingrese datos: ")
    elif menu == "2":
        print(lista_nombres)
    elif menu == "3":
        print("Selecciono salir")
        break
    elif menu == "4":
        lista_nombres.reverse
    else:
        print("Ocpion incorrecta")
