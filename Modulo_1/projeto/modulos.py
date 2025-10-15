print("Exemplo de importação de modulo padrão:")

# Importa o módulo todo
import math 

# Importar apenas o que vai precisar
from math import sqrt

raiz_quadrada = math.sqrt(25)
print(f"A raiz quadrada de 25 é: {raiz_quadrada}")

print("\n Exemplo de criação e utilização de um módulo personalizado")
import meu_modulo
from meu_modulo import saudacao

mensagem = meu_modulo.saudacao("Pedro Lucas")
resultado_dobro = meu_modulo.dobro(5)

print(mensagem)
print(f"O dobro de 5 é: {resultado_dobro}")

# pip3 install requests==2.31.0

print("\nImportação e uso de um módulo de terceiros")
import requests

url = "https://www.exemple.com"
response = requests.get(url)
print(f"Solicitacao HTTP para {url} retornou o status {response.status_code}")