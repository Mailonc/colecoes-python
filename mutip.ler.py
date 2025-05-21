n1 = int(input("digite um numero: "))
op = input("digite uma operação: ")
n2 = int(input("digite outro numero:  ")) 


if op == "+" :
   print (n1 + n2 )

elif op == "-" :
   print(n1 - n2)

elif op == "*" :
   print(n1 * n2)

elif op == "/" :
   print(n1 / n2 )

else:
   print(f"( {op} ) ERRO: você digitou um calculo no momento não pode ser somado ")