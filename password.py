#Reto1 crea una contraseña aleatoria
import random

char = "abcdefghijklmnopqrstuvwxyz1234567890" #Banco de caracteres disponibles
password = "" #Variable donde se guarda la password
dig = 0 #Variable para la cantidad de digitos que vendrán

dig = int(input("Cuantos caracteres debe tener tu password?")) #input para los caracteres a ingresar 

for i in range(dig):
    password += random.choice(char) #ingresar los datos de forma aleatoria elegiendo '.choice' alguno del banco de caracteres '(char)'
    
print("Tu password aleatorio de", dig, " caracteres es: ", password) #Imprimir la contraseña generada
