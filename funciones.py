import os
import msvcrt
import csv
asientos=[["0","0","0","0"],["0","0","0","0"],["0","0","0","0"],["0","0","0","0"],["0","0","0","0"]]
ventas=[]


def limpiar_pantalla():
    os.system("cls")

def esperar_tecla():
    print("presione tecla para continuar")
    msvcrt.getch()

def opcion1():
    i=0
    while i<len(asientos):
        x=0
        while x<len(asientos[i]):
            print(asientos[i][x],end=" ")
            x=x+1
        print("\n")
        i=i+1


def opcion2():
    while True:
        while True:
            try:
                fila=int(input("Ingrese la fila en la que quiere estar: "))
                if fila>=1 and fila<=4:
                    break
                else:
                    print("ERROR esa fila no existe")
            except:
                print("Ingrese numero solamente")
        while True:
            try:
                columna=int(input("Ingrese la columna en la que quiere estar: "))
                if columna<=4 and columna>=1:
                    break
                else:
                    print("ERROR esa columna no existe")
            except:
                print("ingrese nimero solamente")
        i=0
        while i<len(asientos):
            x=0
            while x<len(asientos[i]):
                if fila==i and columna==x and asientos[i][x]=="0":
                    asientos[i-1][x-1]="X"
                x=x+1
            i=i+1
        while True:
            try:
                nombre=input("ingrese su nombre: ")
                if len(nombre)>3:
                    break
                else:
                    print("nombre muy corto")
            except:
                print("ERROR")
        while True:        
            try:
                edad=int(input("ingrese su edad: "))
                if edad>13:
                    break
                else:
                    print("Demasiado joven para comprar")
            except:
                print("ERROR,solo ingrese numeros")
        while True:
            try:
                nro=input("ingrese su numero telefonico: ")
                if len(nro)==8:
                    break
            except:
                print("Error")
        precio_entrada=5000
        if edad>=65:
            precio_entrada=precio_entrada-(precio_entrada*0.15)
        elif edad<=18:
            precio_entrada=precio_entrada-(precio_entrada*0.20)
        
        compra={"nombre":nombre,
                "edad":edad,
                "numero telefonico":nro,
                "precio":precio_entrada,
                "fila":fila,
                "columna": columna}
        ventas.append(compra)
        respuesta=input("Desea seguir comprando?S(si)/N(no)")
        if respuesta.upper()=="N":
            break

    
def opcion3():
    i=0
    total=0
    while i<len(ventas):
        print(ventas[i])
        total=total+ventas[i]["precio"]
        i=i+1
    print("El total de ventas hasta el momento es de ",total)

def opcion4():
    import datetime
    nombre_archivo=str(datetime.datetime.now()).replace(".","").replace(":","").replace(" ","")+".csv"
    print(nombre_archivo)
    with open(nombre_archivo,"w",newline="") as archivo:
        escritor=csv.DictWriter(archivo,["nombre","edad","numero telefonico","precio", "fila","columna"])
        escritor.writeheader()
        escritor.writerows(ventas)
        
    
def opcion5():
    print("Gracias por venir")
    