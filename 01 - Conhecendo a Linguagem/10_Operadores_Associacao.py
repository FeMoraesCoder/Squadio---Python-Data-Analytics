# Operadores de Associação

# %%
curso = "Curso de Python"
nome_curso = curso

print(curso in nome_curso)
print(curso not in nome_curso)

saldo, limite = 200, 200
print(saldo in limite)
print(saldo not in limite)
# %%

saldo = 1000
limite = 500

print(saldo in limite)
print(saldo not in limite)
# %%

curso = "Curso de Python"
frutas = ["Laranja", "Uva", "Limão"]
saques = [1500, 100]

print("Python" in curso)
print("Python" not in curso)

print("Maçã" not in frutas)

# %%

frutas = ["Limão", "Uva"]

print("Laranja" in frutas)
print("limão" in frutas) # Case Sensitive
print("Limão" in frutas) # Case Sensitive

# %%
