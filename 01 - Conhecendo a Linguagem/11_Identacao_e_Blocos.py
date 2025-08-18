'''
A estética

Identar código é uma forma de manter o código fonte mais legível e manutenível. 
Mas em Python ela exerce um segundo papel, através da indentação o interpretador
consegue determinar onde um bloco de comando inicia e onde ele termina.

Bloco de Comando

As linguagem de programação constumam utilizar caracteres ou palavras reservadas para terminar o início e fim do bloco.
Em Java e C por exemplo, utilizamos chaves.

Utilizando espaços

Existe uma convensão em Python, que define as boas práticas
para escrita de código na linguagem. Nesse documento é 
indicado utilizar 4 espaços em branco por nível de indentação,
ou seja, a cada novo bloco adicionamos 4 novos espaços em 
branco.

'''
# Exemplo em Python
#%%
def sacar(valor):
    saldo = 500
    if saldo >= valor:
        print("Valor sacado!")

sacar(100)
#%%