# Verifica que un mail recibido cumpla sus condiciones. 
# Debe empezar con caracteres, seguido de @, más caracteres y debe terminar en .algo (.com, .gob, .mx, .tecnm). 
# example@example.com USA EXPRESIONES REGULARES

import re


user_mail = input("Escribe tu correo\n")

mail = re.search(r'[\w.!&#$%]+_*@[\w.]+\.[a-z]{2,4}',user_mail, flags = re.IGNORECASE) 

if (mail):
    print("Tu mail es válido")
else:
    print("Tu mail NO es válido")