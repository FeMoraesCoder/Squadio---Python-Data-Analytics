'''
Métodos Úteis

A classe String do Python é famosa por ser rica em métodos e possuir uma interface 
muito fácil de trabalhar.
Em algumas linguagens manipular sequências de caracteres não é um trabalho trivial, 
porém, em Python esse trabalho é muito simples.

'''
#%%
# Maiúsculas, Minúsculas e Título

nome = "feLipe"

print(nome.upper())
print(nome.lower())
print(nome.title())

# Eliminando espaços em branco

texto = "   Olá mundo!    "

print(texto + '.')
print(texto.strip() + '.')
print(texto.lstrip() + '.')
print(texto.rstrip() + '.')

# Junções e Centralizações

menu = "Python"

print("####" + menu + "####")
print(menu.center(14))
print(menu.center(14, "#"))

print("P-y-t-h-o-n")
print("-".join(menu))


#%%

#



