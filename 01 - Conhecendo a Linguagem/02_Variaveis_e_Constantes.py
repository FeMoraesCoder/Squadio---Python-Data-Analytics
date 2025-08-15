'''
Variáveis

Em linguagens de programação podemos definir valores que podem
sofrer alterações no decorrer da execução do programa. Esses valores 
recebem o nome de variáveis, pois eles nascem com um valor e não 
necessariamente devem permanecer com o mesmo durante a execução do programa.

'''
#%%
age = 33
name = 'Felipe'
print(f'Meu nome é {name} e eu tenho {age} anos de idades.')

#%%

age, name = (33, 'Felipe')
print(f'Meu nome é {name} e eu tenho {age} anos de idade')

# %%

'''
Alterando valores

Perceba que não precisamos definir o tipo de dados da variável,
o Python faz isso automaticamente para nós. Por isso não podemos simplesmente
criar uma variável sem atribuir um valor. 
Para alterar o valor da variável  basta fazer uma atribuição de um novo valor: 


'''

age = 33
name = 'Felipe'
print(f'Meu nome é {name} e eu tenho {age} anos de idades.')

age = 22
name = 'Moraes'
print(f'Meu nome é {name} e eu tenho {age} anos de idades.')

# %%

'''
Constantes 

Assim com as variáveis, constantes são utilizadas para armazenar valores.
Uma constante nasce com um valor e permanece com ele até o final da execução
do programa, ou seja, o valor é imutável.

Python não tem contantes !!!

Não existe uma palavra reservada para informar ao interpretador que o valor é constante.
Em algumas linguagens por exemplo: Java e C utilizamos final e const, respectivamente para
declarar uma constante.

Em Python usamos a convensão que diz ao programador que a variável é uma constante. Para isso, 
você deve criar a variável com nome todo em letras maiúsculas: 

'''

ABS_PATH = '/home/felipe/Documents/python_course/'
DEBUG = True
STATES = [
    'SP'
    'RJ'
    'MG'
]
AMOUNT = 30.2

'''
BOAS PRÁTICAS: 

> O padrão de nome dever ser snake case;
> Escolher nomes sugestivos;
> Nome de constantes todo em maiúsculo;

'''

limite_saque_diario = 1000 # SnakeCase e Nome Sugestivo
lim_saq_di = 1000 # Snake Case, mas NÃO sugestivo

BRAZILIAN_STATES = ['SP', 'RJ', 'SC', 'MG'] #Constante por convenção


