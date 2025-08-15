'''
Operadores Lógicos

São operadores utilizados em conjunto com os operadores de
comparação, para montar uma expressão lógica. Quando um 
operador de comparação é utilizado, o resultado retornado é 
um booleano, dessa forma podemos combinar operadores de 
comparação com os operadores lógicos, exemplo: 

op_comparacao + op_logico + op_comparacao... N ...

'''
#%%

print(True and True)
print(True and False)
print(True or True)
print(True or False)

#%%

saldo = 1000
saque = 200
limite = 100

# Operador E (and)
saldo >= saque and saque <= limite

#%%
# Operador OU (or)
saldo >= saque or saque >= limite

# %%
# Operador Negação (not)

contatos_emergencia = []

not 1000 > 1500

not contatos_emergencia

not "saque 1500"

not ""
# %%

# Parenteses 

#%%
saldo = 1000
saque = 250
limite = 200
conta_especial = True

saldo >= saque and saque <= limite or conta_especial and saldo >= saque
#%%
saldo = 1000
saque = 250
limite = 200
conta_especial = True

(saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)

#%%





