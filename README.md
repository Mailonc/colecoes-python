# Collections Python
**lists** :
_(list) is a data structure that stores an ordered sequence of values. It is a versatile way to organize and manipulate data, allowing you to add, remove, and modify elements after they are created._. 
```
# Criar uma lista de quadrados dos números de 0 a 9
quadrados = [x**2 for x in range(10)]
print(quadrados)  # Imprime [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Criar uma lista dos números pares de 0 a 10
pares = [x for x in range(11) if x % 2 == 0]
print(pares)  # Imprime [0, 2, 4, 6, 8, 10]

```
**Tuples** :
_(Tuples) A tuple is a data structure that stores an ordered sequence of elements, and is immutable. This means that once created, the tuple cannot be changed (add, remove, or modify elements). To create a tuple, you can use parentheses () and separate the elements by commas._.
```
tupla_acesso = ("a", "b", "c")
print(tupla_acesso[0])  # Output: a
print(tupla_acesso[1])  # Output: b
print(tupla_acesso[2])  # Output: c
# print(tupla_acesso[3])  # IndexError: tupla_acesso não tem índice 3
```
**dictionary**:
_unordered collection of key-value pairs. It is like a traditional dictionary, where words are the keys and their meanings are the values. To create a dictionary, you use curly braces {} to define key-value pairs, which are separated by commas_ 

```
dicionario = {"nome": "Alice", "idade": 25, "cidade": "São Paulo"}`

```
