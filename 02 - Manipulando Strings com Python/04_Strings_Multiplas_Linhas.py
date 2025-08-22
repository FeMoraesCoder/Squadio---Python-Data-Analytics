"""
Strings de múltiplas linhas são definidas informando 3 aspas
simples ou duplas durante a atribuição. Elas podem ocupar
várias linhas do código, e todos os espaços em branco são
incluídos na string final. 

"""
# Strings Triplas ou de Multiplas linhas
#%%
nome = "Felipe"

mensagem = f'''
    Olá meu nome é {nome},
Eu estou aprendendo Python.
    Essa mensagem tem diferentes recuos.
    '''

print(mensagem)
# %%

print(
    """
    ========== MENU ==========

    1 - Depositar
    2 - Sacar
    0 - Sair

    ==========================

        Obrigado por usar nosso sistema !!!
"""
)

# %%
