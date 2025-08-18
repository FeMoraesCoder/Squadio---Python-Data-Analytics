'''
Estruturas Condicionais

A estrutura condicional permite o desvio de fluxo de controle,
quando determinadas expressões lógicas são atendidas.

If

Para criar uma estrutura condicional simples, composta por um 
único desvio, podemos utilizar a palavra reservada if. O 
comando irá testar a expressão lógica, e em caso de retorno
verdadeiro as ações presentes no bloco de código do if serão
executadas.

'''

#%% 
# IF

saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque: 
    print("Realizando saque!")

if saldo < saque:
    print("Saldo insuficiente!")

# %%
'''
IF/ELSE

Para criar uma estrutura condicional com dois desvios, 
podemos utilizar as palavras reservadas if e else. Como
sabemos se a expressão lógica testada no if for verdadeira, 
estão o bloco de código if será executado. Caso contrário o 
bloco de código do else será executado.

'''
saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque: 
    print("Realizando saque!")

else:
    print("Saldo insuficiente!")
# %%

'''
IF, ELIF, ELSE

Em alguns cenários queremos mais de dois desvios, para isso
podemos utlizar a palavra reservada elif. O elif é composto por 
uma nova expressão lógica, que será testada e caso retorne
verdadeiro o bloco de código do elif será executado. Não existe
um número máximo de elifs que podemos utilizar, porém evite
criar grandes estruturas condicionais, pois elas aumentam a
complexidade do código.

'''
#%%
import sys

opcao = int(input("Informe uma opção: [1] sacar \n[2] Extrato: "))

if opcao == 1:
    valor = float(input("Informe a quantia para saque: "))

elif opcao == 2:
    print("Exibindo o extrato...")

else: 
    sys.exit("Opção Inválida")
    
# %%

# ESTRUTURAS CONDICIONAIS

MAIOR_IDADE = 18

idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH")

if idade < MAIOR_IDADE:
    print("Ainda não pode tirar a CNH")

#%%

MAIOR_IDADE = 18

idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Pode tirar a CNH")

else: 
    print("Não pode tirar CNH")

#%%

MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Pode tirar CNH")

elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teóricas, mas não pode fazer aulas práticas.")

else: 
    print("Ainda não pode tirar a CNH.")

#%%

'''
IF ANINHADO

Podemos criar estruturas condiconais aninhadas, para isso 
basta adicionar estruturas if/elif/else dentro do bloco de 
código de estruturas if/elif/else.


'''

conta_normal = True
conta_universitaria = False

saldo = 2000
saque = 500

cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque Realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial!")
    else:
        print("Não foi possível realizar o saque, saldo insuficiente!")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente")
# %%

conta_normal = False
conta_universitaria = True

saldo = 2000
saque = 500

cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque Realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial!")
    else:
        print("Não foi possível realizar o saque, saldo insuficiente!")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso na conta universitária!")
    else:
        print("Saldo insuficiente")
# %%
