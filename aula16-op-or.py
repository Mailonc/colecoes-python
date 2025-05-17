# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser
# verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor

# operador or

# entrada = input('[E]ntrar [S]air: ')
# senha_digitada = input('senha: ')

# senha_permitida =('123456')

# if (entrada == 'E'or entrada == 'e') and senha_digitada == senha_permitida:
#     print('Entrar')
# else:
#     print('Sair') 

# Avaliação de curto Circuito 
# print(True and 0 and True)
# print(True or False)
# print(10 or 'legal' or False or True)

senha = input('senha: ') or 'sem senha'
print(senha)