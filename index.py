import requests #buscar cep
import os #limpar prompt
import time #espera

os.system("cls")
print("Carregando...")

resposta = requests.get("http://localhost/api-cep/") #retorna um aleatório, para específico, passe get ?id=***
os.system("cls")

print(resposta.json())
#     [id,  tipo, palavra, continente, pais, dificuldade]

# Ex: [55, 'cidade', 'Bruges', 'Europa', 'Bélgica', 'dificil']
# Ex: [79, 'país', 'Croácia', 'Europa', None, 'medio']

if resposta.status_code == 200:
    tipo = resposta.json()[1]
    palavra = resposta.json()[2]
    continente = resposta.json()[3]
    pais = resposta.json()[4]
    dificuldade = resposta.json()[5]
    #Aqui continua o jogo
else:
    print("Erro ao acessar a API, escolha outra categoria...")
time.sleep(2)
