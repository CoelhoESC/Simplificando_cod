"""
Operador ternário
"""
# Suponha que a um sistema de login! Esse sistema tem que verificar se o usuario está logado!
logged_user = True
if logged_user:
    msg = 'Usuario logado'
else:
    msg = 'Usuario precisa logar'
print(msg)

# Podemos simplificar esse codigo:
logged_user = True
msg = 'Usuario logado' if logged_user else 'Usuario precisa logar'
print(msg)

# Outro exemplo:
# Verificando se o usuario é maior que 18 anos!
idade = 18
if idade >= 18:
    msg = 'Pode acessar'
else:
    msg = 'Não pode acessar'
print(msg)

# Simplificando o codigo e melhorando!
idade = input('Digite sua idade: ').strip()

if not idade.isnumeric():
    print('Digite apenas um número!!')
else:
    idade = int(idade)
    eh_maior = (idade >= 18)
    msg = 'Pode acessar' if eh_maior else 'Não pode acessar!'
    print(msg)
