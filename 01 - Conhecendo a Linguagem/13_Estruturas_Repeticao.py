'''
Estruturas de Repetição

São estruturas utilizadas para repetir um trecho de código um 
determinado número de vezes. Esse número pode ser 
conhecido previamente ou determinado através de uma expressão
lógica.

Comando FOR

O comando for é usado para percorrer um objeto iterável. Faz
sentido usar for quando sabemos o número exato de vezes que
nosso bloco de código deve ser executado, ou quando
queremos percorrer um objeto iterável.

'''
#%%
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=" ")
else: 
    print() # adiciona uma quebra de linha
# %%

'''
FUNÇÃO RANGE

Range é uma função built-in do Python, ela é usada para
produzir uma sequência de númerso inteiros a partir de um 
ínicip (inclusivo) para um fim (exclusivo). Se usarmos range (i, j)
será produzido:

i, i+1, i+2, i+3, ..., j-1.

Ele recebe 3 argumentos: stop (obrigatório), start (opcional) e 
step (opcional)

'''

# range(stop -> range object)
# range(start, stop[, step]) -> range object

#%%

for numero in range(0, 51, 5):
    print(numero, end=" ")


#%%

'''
Comando While

O comando while é usado para repetir um bloco de código
várias vezes. Faz sentido usar while quando não sabemos o
número exato de vezes que nosso bloco de código deve ser
executado.

'''
opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

    if opcao == 1:
        print('Sacando...')
    elif opcao == 2:
        print("Exibindo o extrato...")
    
# %%

while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break

    print(numero)

# %%
