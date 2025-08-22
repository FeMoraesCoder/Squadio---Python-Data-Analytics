'''
Em python temos 3 formas de interpolar variáveis em strings, a
primeira é usando o sinal %, a segunda é utilizando o método
format e a última é utilizando f strings.

A primeira forma não é atualmente recomendada e seu uso em
Python 3 é raro, por esse motivo iremos focar nas 2 últimas. 

'''


# Old style %

#%% 
nome = "Felipe"
idade = 28
profissao = "Programador"
linguagem = "Python"

print("Ola, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s." % (nome, idade, profissao, linguagem))
# %%

# Método format

nome = "Felipe"
idade = 28
profissao = "Programador"
linguagem = "Python"

print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}.".format(nome, idade, profissao, linguagem))
print("Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho como {1} e estou matriculado no curso de {0}.".format(linguagem, profissao, idade, nome))

# %%

# Método f-string

nome = "Felipe"
idade = 28
profissao = "Programador"
linguagem = "Python"

print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.".format(nome, idade, profissao, linguagem))

#%%

# Formatar Strings com f-string

PI = 3.14159

print(f"Valor de PI: {PI:.2f}")

print(f"Valor de PI: {PI:10.2f}")

# %%

# Todos exemplos: 

nome = "Felipe"
idade = 33
profissao = "Desenvolvedor de RPA"
linguagem = "Python"
saldo = 44.455

dados = {"nome": "Felipe", "idade": 33}

print("Nome: %s Idade: %d" % (nome, idade))

print("Nome: {} Idade: {}".format(nome, idade))

print("Nome: {1} Idade: {0}".format(idade, nome))
print("Nome: {1} Idade: {0} Nome: {1} {1}".format(idade, nome))

print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))
print("Nome: {name} Idade: {age} {name} {name} {age}".format(name=nome, age=idade))
print("Nome: {nome} Idade: {idade}".format(**dados))

print(f"Nome: {nome} Idade: {idade}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:10.1f}")

# %%
