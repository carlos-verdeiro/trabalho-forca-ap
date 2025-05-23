import os
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
╔════════════════════════╗
║      JOGO DA FORCA     ║
╚════════════════════════╝
1 - Jogar
2 - Sair
------------------------
Escolha uma opção: '''

categorias = '''
╔════════════════════════════════════════╗
║         SELEÇÃO DE CATEGORIAS          ║
╚════════════════════════════════════════╝

 [1] Geral
 [2] CEP
 [3] Esporte
 [4] Jogos
 [5] Instrumentos Musicais

------------------------------------------
Digite o número da categoria desejada: '''

os.system("cls")


opt = int(input(menu))
while opt > 2 and opt < 1:
    print("Opção inválida, tente novamente.")
    opt = int(input(menu))
