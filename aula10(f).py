nome = 'mailon cesar'
altura = 1.87
peso = 100
imc = peso / altura ** 2

# print('nome:', nome)
# print('altura:', altura)
# print('peso:', peso)
# print('imc:' ,imc)
 
# exemplo usando fstring

linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)

