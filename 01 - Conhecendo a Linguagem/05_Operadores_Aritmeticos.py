'''
Operadores Aritméticos

Os operadores aritméticos executam operações matemáticas, 
como adição, subtração.

'''
#%%

# Adição, subtração e Multiplicação

print(2 + 2)
print(2 - 3)
print(2 * 2)

# Divisão e divisão inteira

print(12 /  3)
print(12 // 3)

# Módulo e exponenciação

print(10 % 3)
print(10 ** 3)

#%%

'''
Ordem de precedência: 

Na matemática existe uma regra que indica quais operações
devem ser executadas primeiro. Isso é útil pois ao analisar uma
expressão, a depender da ordem das operações o valor pode
ser diferente: 

x = 10 - 5 * 2
x é igual a 10 ou 0? é 0

A definição indica a seguinte ordem como a correta: 
    > Parentesis
    > Expoentes
    > Multiplicações e Divisões (da esquerda para a direita)
    > Somas e Subtrações (da esquerda para a direita)


'''
#%%
produto_1 = 20
produto_2 = 10


print(produto_1 + produto_2 + 3.5)
print(produto_1 - produto_2)
print(produto_1 / produto_2)
print(produto_1 // produto_2)
print(produto_1 * produto_2)
print(produto_1 ** produto_2)

x = (10 + 5) * 4

# Ambos sem o mesmo resultado, mas o segundo é mais legível: 
y = 10 / 2 * 25 * 2 - 2 ** 2
y = (10 / 2) * (25 * 2) - (2 ** 2)

#%%
