#Elabora un “¿Qué probabilidad hay?”, donde el usuario primero ingresa su número, imprimir los resultados.
import random

num_user = 0 #Dato del usuario
num_computer = 0 #Dato random de la computadora
reiniciar = True #Bool para reiniciar juego
resp = '' #Respuesta del usuario si volver a jugar

while(reiniciar):
    num_computer = random.randint(1,3) #Numero random del 1 al 3

    num_user = int(input("\nQue probabilidad hay del 1 al 3\n")) #Input del dato del usuario

    print("\nEl numero que has elegido es: ", num_user, "\nEl numero que ha elegido la computadora es: ", num_computer)

    if(num_user == num_computer): #Comparador de numeros
        print("Los numeros son iguales, has ganado!") #Si son iguales gana
    else:
        print("Los numeros no son iguales, has perdido") #Si no son iguales pierde
    
    resp = input("\nDeseas volver a jugar? Si/No\n").upper() #.upper() para volver mayuscula su respuesta
    
    if(resp == 'SI'): #Reiniciar juego
        reiniciar = True
    elif(resp == 'NO'): #Cancelar juego
        reiniciar = False
        
print("\nJuego finalizado con exito")