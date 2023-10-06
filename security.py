# Crea un programa que verifique si una contraseña cumple ciertos criterios de seguridad. 
# Por ejemplo que lleve mayúsculas, números o un mínimo de caracteres.

import re #libreria a para expreziones regulares, sirven para verificar contraseñas

user_password = ''
contador = 0

print("\nLa contraseña debe ser mayor a 6 caracteres, minimo 1 numero, 1 letra mayuscula, 1 letra minuscula y minimo un caracter especial")
user_password = input("Para verificar que tu contraseña cumple con los requisitos de seguridad\nescribe tu contraseña: \n")


num_caracters = len(user_password) #Contador de caracteres en la cadena
digit = re.search(r'\d+', user_password) #re.search(r'\d+') sirve para encontrar uno o mas digitos
mayus = re.search(r'[A-Z]+', user_password) #re.search(r'[A-Z]+') sirve para encontrar letras mayusc
minus = re.search(r'[a-z]+', user_password) #re.search(r'[a-z]+') sirve para encontrar letras minusc
char = re.search(r'\W', user_password) #re.search(r'\W') sirve para encontrar TODO menos alfanumericos(caracteres especiales)


if num_caracters:
    print("1. Tu contraseña tiene el numero minimo de caracteres")
    contador +=1
else:
    print("1. Tu contraseña no tiene el numero minimo de caracteres")
    
if digit:
    print("2. Tu contraseña tiene al menos un numero")
    contador +=1
else:
    print("2. Tu contraseña no tiene al menos un numero")
     
if mayus:
    print("3. Tu contraseña tiene al menos una letra mayuscula")
    contador +=1
else:
    print("3. Tu contraseña no tiene al menos una letra mayuscula")
       
if minus:
    print("4. Tu contraseña tiene al menos una letra minuscula")
    contador +=1
else:
    print("4. Tu contraseña no tiene al menos una letra minuscula")
    
if char:
    print("5. Tu contraseña tiene al menos un caracter especial")
    contador +=1
else:
    print("5 Tu contraseña no tiene al menos un caracter especial") 

if contador == 5:
    print("*Tu contraseña es segura*") 
else:
    print("*Tu contrasña no es segura*")
    
