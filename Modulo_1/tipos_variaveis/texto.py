# Declaracao 
nome_completo = "Pedro Lucas"

# Declaração que pode pular linha
nome_completo_2 = """Pedro
LUCAS"""

nome_completo_3 = "Pedro \
Lucas"

nome = "Pedro"
sobrenome = "Moreira"

# Formatação
print("Nome completo (1ª Forma):", nome_completo)
print("Nome completo (2ª Forma):" + nome_completo) # Concatenação
print("Nome completo (3ª Forma):" + "Pedro" + "Moreira") # Concatenação
print("Nome completo (4ª Forma):" + "Pedro", "Moreira") # Concatenação
print("Nome completo (5ª Forma):", nome_completo_2)
print("Nome completo (6ª Forma):", nome_completo_3)
print("Nome completo (7ª Forma): %s" % nome)
print("Nome completo (8ª Forma): %s %s" % (nome, sobrenome))
print(f"Nome completo (9ª Forma): {nome} {sobrenome}")
print("Nome completo (10ª Forma): {} {}".format(nome, sobrenome))

# Métodos de Strings
print(nome.upper())
print(nome.lower())
print(nome_completo.count("o")) # Contar caracteres
print(nome_completo.find("o")) # Encontrar caracteres (posição)
print(nome_completo.encode()) # Codificar em bytes
print(nome_completo.encode().decode()) # Decodificar em bytes
print(nome_completo.replace("e", "3")) # Substituir caracteres
