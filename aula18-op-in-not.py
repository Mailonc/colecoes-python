# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5
#  O t á v i o
# -6-5-4-3-2-1

nome = ('mailon')
# print(nome[3])
# print(nome[-3])
# print('mai' not in nome)
# print('ju' not in nome)

nome = input('digite seu nome: ')
encontrar = input('o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} esta em {nome}')
else:
    print(f'{encontrar} não esta em {nome}')

