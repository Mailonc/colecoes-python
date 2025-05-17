# projeto que reproduz o seu signo com dia e mes de seu nascimento.

import time, sys, os
os.system('clear')

dia = int(input("digite o dia de nascimento(1-31): "))
mes = int(input("digite o mes do seu nascimento(1-12): "))

if dia>=20 and dia<=31 and mes == 3 or dia>=1 and dia<=20 and mes==4:
    print('seu signo é aries')
elif dia>=21 and dia<=30 and mes==4 or dia>=1 and dia<=20 and mes==5:
    print ("Seu Signo é de Touro")
elif dia>=21 and dia<=30 and mes==5 or dia>=1 and dia<=20 and mes==6:
    print('gemios')
    
    