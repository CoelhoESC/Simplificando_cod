"""
Expressão condicional com operador OR
"""
nome = input('Qual é seu nome: ')

if nome:
    print(nome)
else:
    print('Você não digitou nada!')

# Usando o operador OR(ou) para simplicar!
print(nome or 'Você não digitou nada!')

# OR para na primeira expressão TRUE
print(nome or None or False or 0 or 'Você não digitou nada!' or 'Outra coisa')
#              F        F      F            V = 1° True                V


# Simplicando para não fazer uma condição enorme!
a = 0
b = False
c = None
d = []
e = {}
f = 'Everton'
g = 22

variavel = a or b or c or d or e or f or g

# Simplificando para não fazer isso:
if a:
    variavel = a
elif b:
    variavel = b
