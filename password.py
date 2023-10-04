#Reto1 crea una contraseña aleatoria
import random

char = "abcdefghijklmnopqrstuvwxyz1234567890"
password = ""
dig = 0

dig = int(input("Cuantos caracteres debe tener tu password?"))

for i in range(dig):
    password += random.choice(char)
    
print("Tu password aleatorio de", dig, " caracteres es: ", password)