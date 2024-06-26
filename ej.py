

from funciones import *

while True:
    limpiar_pantalla()
    print("Cine Hoyt")
    print("Elprecio de las entradas es de $5000 con ")
    print(" descuento para adultos mayores y niños")
    print("1-mostrar asientos")
    print("2-comprar entrada")
    print("3-Mostrar ventas")
    print("4-Mostrar archivo csv")
    print("5-Salir")
    while True:
        try:
            opcion=int(input("ingrese opcion desable: "))
            if opcion>0 and opcion<6:
                break
            else:
                print("Error")
        except:
            print("Opcion no valida")

    if opcion==1:
        opcion1()
        esperar_tecla()
    elif opcion==2:
        opcion2()
        esperar_tecla()
    elif opcion==3:
        opcion3()
        esperar_tecla()
        
    elif opcion==4:
        opcion4()
        esperar_tecla()
    else:
        opcion5()
        break