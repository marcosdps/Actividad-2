import csv
from clase import ViajeroFrecuente


def leerDatos(archi):
    reader = csv.reader(archi, delimiter= ",")
    for fila in reader:
        unViajero = ViajeroFrecuente(0,0,"","",0)
        unViajero.leerDatos(fila)
        unViajero.mostrarDatos()
        lista.append(unViajero)
    print(len(lista))
    

def menu():
    print("\n--------MENÚ DE OPCIONES--------")
    print("-1- Consultar Cantidad de Millas")
    print("-2- Acumular Millas")
    print("-3- Canjear Millas")
    print("-0- Salir")
    x = int(input("Ingrese opcion:")) #sin el cast por alguna razon me returna none en vez de 0, por lo que nunca sale
    return x


def buscoIndice(numIngresadoViajero): #BUSQUEDA SIEMPRE CON WHILE!!
    indice = 0
    i=0
    while indice == 0:
        resultado = lista[i].comparoNumeros(numIngresadoViajero)
        if resultado == 1:
            return i
        i +=1
    if resultado == -1:
        print("Numero ingresado incorrecto")
        return resultado

"""def buscoIndice(numIngresadoViajero):
    indice =0
    i=0
    while indice == 0:
        indice = lista[i].buscarObjeto(numIngresadoViajero)
        i += 1
    return indice"""
    

def seleccion(opcion, indice):#------------switch del menu----------
    if opcion == 1:
        print(f"Usted tiene un total de {lista[indice].cantidadTotaldeMillas()} millas acumuladas") 
    elif opcion == 2:
        millasRecorridas = float(input("Ingrese la cantidad de millas recorridas: "))
        lista[indice].acumularMillas(millasRecorridas)
        print("Millas añadidas")
    elif opcion == 3:
        millasAcanjear = float(input("Ingrese la cantidad de millas que desea canjear: "))
        lista[indice].canjearMillas(millasAcanjear)


if __name__ == '__main__':
    lista = []
    archi = open("aerolineas.csv")
    #------------Pto 1__LECTURA DE DATOS----------------
    leerDatos(archi)
    for i in range(len(lista)):
        print(i)
        lista[i].mostrarDatos()
    #------------Pto 2__MENU-------------
    #numViajeroFrec = input("Ingrese numero de viajero frecuente: ")
    opcion = -1
    indice = -1
    while indice == -1:#verifico numero de viajero ingresado
        numIngresadoViajero = int(input("Ingrese su numero de viajero frecuente: "))
        indice = buscoIndice(numIngresadoViajero) #Busco la instancia perteneciente al numero ingresado
    
    while opcion != 0:
        opcion = menu()
        seleccion(opcion, indice)
        if opcion == 0:
            print("SALIENDO...")
        