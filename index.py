import os #limpar prompt
import time #espera
import random #escolher palavra aleatória

forca = ['''
┌──────┐
│      │
│
│
│
│
│
      ''','''
┌──────┐
│     ┌─┐
│     └─┘
│      
│
│
│
      ''','''
┌──────┐
│     ┌─┐
│     └─┘
│     /│
│      │ 
│
│
      ''','''
┌──────┐
│     ┌─┐
│     └─┘
│     /│\\
│      │ 
│
│
      ''','''
┌──────┐
│     ┌─┐
│     └─┘
│     /│\\
│      │ 
│     / 
│
      ''','''
┌──────┐
│     ┌─┐
│     └─┘
│     /│\\
│      │ 
│     / \\
│
      ''','''
┌──────┐
│     ┌─┐
│     └─┘
│    ═════
│     /│\\
│      │ 
│     / \\
    ░░░░░░░░
      ''']

# chame usando print(forca[*])

menu = '''
\033[36m╔════════════════════════╗\033[m
\033[36m║\033[m      \033[38mJOGO DA FORCA\033[m     \033[36m║\033[m
\033[36m╚════════════════════════╝\033[m
1 - Jogar
2 - Sair
------------------------
Escolha uma opção: '''

categorias = '''
\033[36m╔════════════════════════════════════════╗\033[m
\033[36m║\033[m         \033[38mSELEÇÃO DE CATEGORIAS \033[m         \033[36m║\033[m
\033[36m╚════════════════════════════════════════╝\033[m

 [1] Geral
 [2] CEP
 [3] Esporte
 [4] Jogos
 [5] Instrumentos Musicais

------------------------------------------
Digite o número da categoria desejada: '''


os.system("cls")

opt = input(menu)
while not opt.isdigit() or int(opt) > 2 or int(opt) < 1:
      os.system("cls")
      print("\033[31mOpção inválida, tente novamente.\033[m")
      opt = input(menu)

opt = int(opt)

pontuacao = 0
erros = 0

if opt == 1:
      os.system("cls")
      cat = input(categorias)
      while not cat.isdigit() or int(cat) > 5 or int(cat) < 1:
            os.system("cls")
            print("\033[31mOpção inválida, tente novamente.\033[m")
            cat = input(categorias)
      cat = int(cat)
      
      if cat == 1:
            #geral
            categoria = "Geral"
            print("Geral")
      elif cat == 2:
            #cep
            categoria = "CEP"
            palavras = [
            ['Brasil', 'América do Sul',1],
            ['Canadá', 'América do Norte',1],
            ['Madagascar', 'África',2],
            ['Cazaquistão', 'Ásia',3],
            ['Islândia', 'Europa',2],
            ['Quirguistão', 'Ásia',3],
            ['Butão', 'Ásia',2],
            ['Liechtenstein', 'Europa',3],
            ['Croácia', 'Europa',2],
            ['Uruguai', 'América do Sul',1],
            ['Egito', 'África',1],
            ['Chade', 'África',3],
            ['Eslováquia', 'Europa',3],
            ['Togo', 'África',1],
            ['Zâmbia', 'África',2],
            ['Alasca', 'América do Norte',2],
            ['Tasmânia', 'Oceania', 3],
            ['Quebec', 'América do Norte', 2],
            ['Andaluzia', 'Europa', 3],
            ['Baviera', 'Europa', 2],
            ['Califórnia', 'América do Norte', 1],
            ['Punjab', 'Ásia', 2],
            ['Galícia', 'Europa', 3],
            ['Guarani', 'América do Sul', 2],
            ['Hokkaido', 'Ásia', 3],
            ['Tóquio', 'Ásia', 1],
            ['Nairobi', 'África', 2],
            ['Zurique', 'Europa', 2],
            ['Recife', 'América do Sul', 1],
            ['Edimburgo', 'Europa', 3],
            ['Valparaíso', 'América do Sul', 2],
            ['Istambul', 'Europa/Ásia', 2],
            ['Ljubljana', 'Europa', 3],
            ['Córdoba', 'América do Sul', 2],
            ['Bruges', 'Europa', 3],
            ['Cracóvia', 'Europa', 2],
            ['Arequipa', 'América do Sul', 2],
            ['Manágua', 'América Central', 2],
            ['Chiang Mai', 'Ásia', 2],
            ['Xangai', 'Ásia', 1],
            ['Osasco', 'América do Sul', 1],
            ['Mendoza', 'América do Sul', 2],
            ['Helsinque', 'Europa', 2],
            ['Gênova', 'Europa', 2],
            ['Cusco', 'América do Sul', 2],
            ['Cusco', 'América do Sul', 2],
            ['Galícia', 'Europa', 3],
            ['Liechtenstein', 'Europa', 3],
            ['Baviera', 'Europa', 2],
            ['Zâmbia', 'África', 2],
            ['Liechtenstein', 'Europa', 3],
            ['Tóquio', 'Ásia', 1],
            ['Ljubljana', 'Europa', 3],
            ['Recife', 'América do Sul', 1],
            ['Bruges', 'Europa', 3],
            ['Eslováquia', 'Europa', 3],
            ['Hokkaido', 'Ásia', 3],
            ['Alasca', 'América do Norte', 2],
            ['Xangai', 'Ásia', 1],
            ['Tasmânia', 'Oceania', 3],
            ['Quebec', 'América do Norte', 2],
            ['Madagascar', 'África', 2],
            ['Galícia', 'Europa', 3],
            ['Butão', 'Ásia', 2],
            ['Istambul', 'Europa/Ásia', 2],
            ['Hokkaido', 'Ásia', 3],
            ['Manágua', 'América Central', 2],
            ['Brasil', 'América do Sul', 1],
            ['Canadá', 'América do Norte', 1],
            ['Madagascar', 'África', 2],
            ['Liechtenstein', 'Europa', 3],
            ['Alasca', 'América do Norte', 2],
            ['Andaluzia', 'Europa', 3],
            ['Califórnia', 'América do Norte', 1],
            ['Liechtenstein', 'Europa', 3],
            ['Quebec', 'América do Norte', 2],
            ['Cusco', 'América do Sul', 2],
            ['Punjab', 'Ásia', 2],
            ['Croácia', 'Europa', 2],
            ['Islândia', 'Europa', 2],
            ['Quirguistão', 'Ásia', 3],
            ['Cracóvia', 'Europa', 2],
            ['Cusco', 'América do Sul', 2],
            ['Osasco', 'América do Sul', 1],
            ['Gênova', 'Europa', 2],
            ['Helsinque', 'Europa', 2],
            ['Madagascar', 'África', 2],
            ['Islândia', 'Europa', 2],
            ['Galícia', 'Europa', 3],
            ['Canadá', 'América do Norte', 1],
            ['Recife', 'América do Sul', 1],
            ['Chiang Mai', 'Ásia', 2],
            ['Quebec', 'América do Norte', 2],
            ['Ljubljana', 'Europa', 3],
            ['Cracóvia', 'Europa', 2],
            ['Califórnia', 'América do Norte', 1],
            ['Canadá', 'América do Norte', 1],
            ['Quebec', 'América do Norte', 2],
            ['Galícia', 'Europa', 3],
            ['Xangai', 'Ásia', 1],
            ['Helsinque', 'Europa', 2],
            ['Cusco', 'América do Sul', 2],
            ['Islândia', 'Europa', 2],
            ['Tasmânia', 'Oceania', 3],
            ['Islândia', 'Europa', 2],
            ['Andaluzia', 'Europa', 3],
            ['Galícia', 'Europa', 3],
            ['Ljubljana', 'Europa', 3],
            ['Edimburgo', 'Europa', 3],
            ['Cazaquistão', 'Ásia', 3]
            ]
      elif cat == 3:
            #esporte
            categoria = "Esporte"
            print("Esporte")
      elif cat == 4:
            #jogos
            categoria = "Jogos"
            print("Jogos")
      elif cat == 5:
            #instrumentos_musicais
            categoria = "Instrumentos musicais"
            print("Instrumentos musicais")
      

      os.system("cls")
      
      selecionada = random.choice(palavras)
      print(selecionada)
      palavra = selecionada[0]
      dificuldade = "Fácil" if selecionada[2] == 1 else "Médio" if selecionada[2] == 2 else "Difícil"
      
      print(f"Categoria: {categoria} | Dificuldade: {dificuldade}")
      
      
      
      
      
      
      
else:
      os.system("cls")
      print("\033[31mSaindo...\033[m")
