# Implementa un algoritmo de ordenamiento para ordenar una lista de números ingresada por el usuario.
# Ya sea de mayor a menor o menor a mayor.

array = [] #Aqui se guarda la original
new_array = [] #La nueva ordenada
flag = True

dimension = int(input("\nIngresa la dimension de los datos a ingresar\n")) #Dale entrada al espacio de tu array

for i in range(dimension):
    print("\nIngresa el dato en tu array no: ", (i+1))
    elemento = int(input("")) #Guarda el dato dado por el usuario
    array.append(elemento) #añade el elemento al array original
    
while(flag):
    resp = int(input("\nComo quieres ordenar tu array?\n1: Menor a mayor\n2: Mayor a menor\n")) #Pregunta de que forma ordenar el array.
    
    if(resp == 1):
        new_array = sorted(array) #sorted(array) ordena una nueva array
        print("Tu nuevo array ordenado de menor a mayor es: ", new_array)
        flag = False
    elif(resp == 2):
        flag = False
        new_array = sorted(array, reverse = True) #sorted(array, reverse=True) ordena el array de manera inversa
        print("Tu nuevo array ordenado de menor a mayor es: ", new_array)
    else:
        print("Tu respuesta no es valida, intentalo de nuevo\n")

