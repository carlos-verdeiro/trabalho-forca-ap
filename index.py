import os #limpar prompt
import time #espera
import random #escolher palavra aleatória
import unicodedata, re #remover acentos

forca = ['''┌──────┐
│      │
│
│
│
│
│''','''┌──────┐
│     ┌─┐
│     └─┘
│      
│
│
│''','''┌──────┐
│     ┌─┐
│     └─┘
│      │
│      │ 
│
│''','''┌──────┐
│     ┌─┐
│     └─┘
│     /│
│      │ 
│
│''','''┌──────┐
│     ┌─┐
│     └─┘
│     /│\\
│      │ 
│
│''','''┌──────┐
│     ┌─┐
│     └─┘
│     /│\\
│      │ 
│     / 
│''','''┌──────┐
│     ┌─┐
│     └─┘
│     /│\\
│      │ 
│     / \\
│''','''┌──────┐
│     ┌─┐
│     └─┘
│    ═════
│     /│\\
│      │ 
│     / \\
    ░░░░░░░░''']

# chame usando print(forca[*])

menu = '''
\033[36m╔════════════════════════╗\033[m
\033[36m║\033[m      \033[38mJOGO DA FORCA\033[m     \033[36m║\033[m
\033[36m╚════════════════════════╝\033[m
[1] Jogar
[2] Sair
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
 [6] Voltar

------------------------------------------
Digite o número da categoria desejada: '''


os.system("cls")

opt = input(menu)
while not opt.isdigit() or int(opt) > 2 or int(opt) < 1:
      os.system("cls")
      print("\033[31mOpção inválida, tente novamente.\033[m")
      opt = input(menu)

opt = int(opt)
while opt != 2:
    os.system("cls")
    cat = input(categorias)
    while not cat.isdigit() or int(cat) > 6 or int(cat) < 1:
        os.system("cls")
        print("\033[31mOpção inválida, tente novamente.\033[m")
        cat = input(categorias)
    cat = int(cat)
    os.system('cls')
    while cat != 6:

        if cat == 1:
            #geral
            categoria = "Geral"
            print("Geral")
        elif cat == 2:
            #cep
            categoria = "CEP"
            palavras = [
            ['Brasil', 'América do Sul', 1],
            ['Canadá', 'América do Norte', 1],
            ['Madagascar', 'África', 2],
            ['Cazaquistão', 'Ásia', 3],
            ['Islândia', 'Europa', 2],
            ['Quirguistão', 'Ásia', 3],
            ['Butão', 'Ásia', 2],
            ['Liechtenstein', 'Europa', 3],
            ['Croácia', 'Europa', 2],
            ['Uruguai', 'América do Sul', 1],
            ['Egito', 'África', 1],
            ['Chade', 'África', 3],
            ['Eslováquia', 'Europa', 3],
            ['Togo', 'África', 1],
            ['Zâmbia', 'África', 2],
            ['Alasca', 'América do Norte', 2],
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
            ['Argentina', 'América do Sul', 1],
            ['Chile', 'América do Sul', 1],
            ['Colômbia', 'América do Sul', 1],
            ['Peru', 'América do Sul', 1],
            ['Bolívia', 'América do Sul', 2],
            ['Equador', 'América do Sul', 2],
            ['Paraguai', 'América do Sul', 2],
            ['Venezuela', 'América do Sul', 1],
            ['México', 'América do Norte', 1],
            ['Estados Unidos', 'América do Norte', 1],
            ['Cuba', 'América Central', 2],
            ['Jamaica', 'América Central', 2],
            ['Haiti', 'América Central', 3],
            ['República Dominicana', 'América Central', 2],
            ['Panamá', 'América Central', 2],
            ['Costa Rica', 'América Central', 2],
            ['Honduras', 'América Central', 3],
            ['Nicarágua', 'América Central', 3],
            ['El Salvador', 'América Central', 3],
            ['Guatemala', 'América Central', 3],
            ['Reino Unido', 'Europa', 1],
            ['França', 'Europa', 1],
            ['Alemanha', 'Europa', 1],
            ['Itália', 'Europa', 1],
            ['Espanha', 'Europa', 1],
            ['Portugal', 'Europa', 1],
            ['Grécia', 'Europa', 2],
            ['Turquia', 'Europa/Ásia', 2],
            ['Rússia', 'Europa/Ásia', 1],
            ['Polônia', 'Europa', 2],
            ['Hungria', 'Europa', 3],
            ['Áustria', 'Europa', 2],
            ['Suíça', 'Europa', 1],
            ['Bélgica', 'Europa', 2],
            ['Holanda', 'Europa', 2],
            ['Dinamarca', 'Europa', 2],
            ['Suécia', 'Europa', 2],
            ['Noruega', 'Europa', 2],
            ['Finlândia', 'Europa', 2],
            ['Irlanda', 'Europa', 2],
            ['África do Sul', 'África', 1],
            ['Nigéria', 'África', 1],
            ['Marrocos', 'África', 2],
            ['Argélia', 'África', 2],
            ['Tunísia', 'África', 2],
            ['Quênia', 'África', 2],
            ['Tanzânia', 'África', 2],
            ['Uganda', 'África', 3],
            ['Etiópia', 'África', 3],
            ['Gana', 'África', 2],
            ['Senegal', 'África', 2],
            ['Angola', 'África', 2],
            ['Moçambique', 'África', 2],
            ['Zimbábue', 'África', 3],
            ['Índia', 'Ásia', 1],
            ['China', 'Ásia', 1],
            ['Japão', 'Ásia', 1],
            ['Coreia do Sul', 'Ásia', 1],
            ['Indonésia', 'Ásia', 1],
            ['Tailândia', 'Ásia', 2],
            ['Vietnã', 'Ásia', 2],
            ['Filipinas', 'Ásia', 2],
            ['Malásia', 'Ásia', 2],
            ['Singapura', 'Ásia', 1],
            ['Arábia Saudita', 'Ásia', 2],
            ['Emirados Árabes Unidos', 'Ásia', 1],
            ['Irã', 'Ásia', 2],
            ['Iraque', 'Ásia', 3],
            ['Paquistão', 'Ásia', 2],
            ['Afeganistão', 'Ásia', 3],
            ['Nepal', 'Ásia', 3],
            ['Sri Lanka', 'Ásia', 3],
            ['Bangladesh', 'Ásia', 3],
            ['Austrália', 'Oceania', 1],
            ['Nova Zelândia', 'Oceania', 1],
            ['Fiji', 'Oceania', 3],
            ['Samoa', 'Oceania', 3],
            ['Vanuatu', 'Oceania', 3],
            ['Tonga', 'Oceania', 3],
            ['Palau', 'Oceania', 3],
            ['Nauru', 'Oceania', 3],
            ['Kiribati', 'Oceania', 3],
            ['Tuvalu', 'Oceania', 3],
            ['Ilhas Marshall', 'Oceania', 3],
            ['Micronésia', 'Oceania', 3],
            ['Papua Nova Guiné', 'Oceania', 2],
            ['Ilhas Salomão', 'Oceania', 3],
            ['Timor-Leste', 'Ásia', 3],
            ['Geórgia', 'Europa/Ásia', 2],
            ['Armênia', 'Europa/Ásia', 3],
            ['Azerbaijão', 'Europa/Ásia', 3],
            ['Chipre', 'Europa/Ásia', 3],
            ['Malta', 'Europa', 3],
            ['Luxemburgo', 'Europa', 3],
            ['Andorra', 'Europa', 3],
            ['Mônaco', 'Europa', 3],
            ['San Marino', 'Europa', 3],
            ['Cidade do Vaticano', 'Europa', 3],
            ['Kosovo', 'Europa', 3],
            ['Montenegro', 'Europa', 3],
            ['Albânia', 'Europa', 3],
            ['Macedônia do Norte', 'Europa', 3],
            ['Sérvia', 'Europa', 3]
            ]
        elif cat == 3:
            #esporte
            categoria = "Esporte"
            palavras = [
            ["Esgrima", "Esporte olímpico em que duas pessoas lutam com 'palitos de dente'", 1],
            ["Pancrácio", "Luta grega", 2],
            ["Hipismo", "Adestramento de equinos", 2],
            ["Levantamento de peso", "Muita força e careta", 2],
            ["Tiro esportivo", "Turco com a mão no bolso", 1],
            ["Tiro com arco", "Acertar a bolinha vermelha", 2],
            ["Triatlo", "Combinação aeróbica", 3],
            ["Golfe", "Carrinho de ?", 1],
            ["Patinação", "Frozen", 1],
            ["Hóquei no gelo", "Gelo e marmanjo", 2],
            ["Snowboard", "Manobras na neve", 1],
            ["Skate", "Equilíbrio e hematomas", 1],
            ["Pólo", "Perfume", 1],
            ["Sumô", "Não saia do círculo", 3],
            ["Futebol", "2 defensores", 1],
            ["Rúgbi", "Parece futebol americano", 2],
            ["Surfe", "Tubarão", 3],
            ["Caratê", "Quebro tijolos", 3],
            ["Remo", "Rômulo e ?", 2],
            ["Canoagem", "Os Guarani usavam", 2],
            ["Xadrez", "Piso de cozinha", 3],
            ["Parkour", "Pula e não morre", 2],
            ["Orientação", "Mapas, bússolas em busca de algo", 3],
            ["Kitesurf", "Pipa e prancha", 1],
            ["Fisiculturismo", "Só o suco", 1],
            ["Skeleton", "Trenó e fé", 3],
            ["E-sports", "Online", 2],
            ["Esporte de lenhador", "Madeeeiraaa", 3],
            ["Boxe", "Muito jab", 1],
            ["Atletismo", "Corra, salte, lance e marche", 1],
            ["Natação", "Atletas parecem focas", 1],
            ["Pólo aquático", "Água com gol", 1],
            ["MMA", "Luta mista", 1],
            ["Judô", "Não bata as costas no chão", 1],
            ["Tênis de mesa", "Sapato na mesa", 1],
            ["Basquete", "190 cm é o mínimo", 1]
]

        elif cat == 4:
            #jogos
            categoria = "Jogos"
            print("Jogos")
        elif cat == 5:
            #instrumentos_musicais
            categoria = "Instrumentos musicais"
            palavras = [
            ["Violão", "Muito usado em rodas de amigos", 1],
            ["Guitarra", "Quebra em shows", 1],
            ["Violoncelo", "Muito usado em orquestras", 1],
            ["Viola", "É pequeno", 1],
            ["Cavaquinho", "Muito usado no pagode", 1],
            ["Flauta", "É tocada com a boca", 1],
            ["Clarinete", "Possui palheta simples e corpo cilíndrico", 1],
            ["Saxofone", "Muito usado no jazz", 2],
            ["Trompete", "Possui três pistões", 2],
            ["Trombone", "Muito usado em fanfarras e orquestras", 2],
            ["Fagote", "Tem um tubo comprido dobrado sobre si mesmo", 2],
            ["Oboé", "Palheta dupla e som agudo e penetrante", 3],
            ["Corneta", "Parece uma trombeta, mas é mais curta e com som mais suave", 2],
            ["Trompa", "Seu tubo é enrolado e tem um som aveludado", 3],
            ["Tuba", "Muito usada em bandas marciais", 3],
            ["Gaita de fole", "Instrumento típico da Escócia", 1],
            ["Bateria", "Conjunto de tambores e pratos", 1],
            ["Tambor", "Tocado com baquetas ou mãos", 1],
            ["Pandeiro", "Possui pequenos pratos que produzem som metálico", 1],
            ["Surdo", "O que acontece quando se perde a audição?", 2],
            ["Caixa", "Caixa Econômica Federal", 2],
            ["Xilofone", "A baqueta tem ponta redonda", 3],
            ["Vibrafone", "Usado no jazz e na música contemporânea", 3],
            ["Marimba", "Parecida com o xilofone, mas com teclas maiores", 3],
            ["Cuíca", "Instrumento de fricção usado no samba", 2],
            ["Reco-reco", "Feito inteiramente de madeira", 2],
            ["Mandola", "Instrumento de cordas semelhante ao bandolim", 3],
            ["Sitar", "Tubarão-serra", 3],
            ["Ukulele", "Pequeno instrumento de cordas havaiano", 2],
            ["Hang drum", "Parece um OVNI", 3],
            ["Stylophone", "Pequeno sintetizador tocado com uma caneta metálica", 3],
            ["Berimbau", "Muito usado na capoeira", 1],
            ["Ehecachichtli", "Produz sons que imitam a morte", 3],
            ["Pokeflauta", "Famosa no universo Pokémon", 1],
            ["Kalimba", "Também chamada de piano de dedo", 3],
            ["Didgeridoo", "Tem dois metros", 3],
            ["Harpa", "Cupido", 1],
            ["Ocarina", "Jogo Zelda", 2],
            ["Guzheng", "Tocado com unhas postiças", 3],
            ["Erhu", "É usada pele de cobra na sua fabricação", 3],
            ["Agogô", "Sino de vaca", 3],
            ["Castanhola", "Fruta", 3],
            ["Cítara", "Instrumento de cordas plano, muito usado no zodíaco", 3],
            ["Acordeon", "Luiz Gonzaga", 2],
            ["Órgão", "Muito usado em igrejas", 1],
            ["Piano", "Beethoven", 1],
            ["Prato", "Não é usado para comer", 1],
            ["Xequerê", "Cabaça seca, coberta por uma rede", 3],
            ["Gunga", "Jogador de tênis", 2],
            ["Triângulo", "Forma geométrica", 1]
            ]

        erros = 0
        jogadas = []
        fim = False
        dica = False
        
        selecionada = random.choice(palavras)
        palavra = unicodedata.normalize('NFD', selecionada[0].upper()).encode('ascii', 'ignore').decode('utf-8')
        dificuldade = "Fácil" if selecionada[2] == 1 else "Médio" if selecionada[2] == 2 else "Difícil"
        dig = []
        for letra in palavra:
            if letra == " ":
                dig.append(" ")
            elif letra == "-":
                dig.append("-")
            else:
                dig.append("_")
        print(palavra)
        
        while not fim:
            os.system("cls")
            print(f"\033[36m{categoria}\033[m")
            print(f"{dificuldade} | Letras: {len(palavra)}")
            if len(jogadas) > 0:
                print(f"Jogadas: {' - '.join(jogadas)}")
            if dica:
                print(f"\033[33mDica: {selecionada[1]}\033[m")

            print(forca[erros])
            
            print(" ".join(dig))
            digitado = ""
            if dica or erros > 5: 
                digitado = input('''\nDigite uma letra ou a palavra completa: ''')
            else:
                digitado = input('''\nDigite uma letra ou a palavra completa, 5 para dica(-1 vida): ''')
                
            if digitado.isdigit():
                if dica:
                    print("\033[31mVocê já pediu uma dica.\033[m")
                elif erros > 5:
                    print("\033[31mVocê não pode mais pedir a dicas.\033[m")
                else:
                    dica = True
                    erros += 1
            else:
                digitado = unicodedata.normalize('NFD', digitado.upper()).encode('ascii', 'ignore').decode('utf-8')
                if len(digitado) == 1 and re.match("^[A-Z]$", digitado):
                    if digitado in jogadas:
                        print("\033[31mVocê já tentou essa letra.\033[m")
                    elif digitado in palavra:
                        jogadas.append(digitado)
                        for p in range(len(palavra)):
                            if palavra[p] == digitado:
                                dig[p] = digitado
                    else:
                        jogadas.append(digitado)
                        erros += 1
                        print("\033[31mLetra incorreta.\033[m")
                elif len(digitado) > 1:
                    if digitado == palavra:
                        fim = True
                        print(f"\033[32mParabéns, você acertou a palavra {selecionada[0]}!\033[m")
                    else:
                        erros += 1
                        print("\033[31mPalavra incorreta.\033[m")
                else:
                    print("\033[31mEntrada inválida. Digite uma letra ou a palavra completa.\033[m")  
            
            if erros > 6:
                fim = True
                print(f"\033[31mVocê perdeu! A palavra era: {selecionada[0]}\033[m")
                time.sleep(2)
            elif "_" not in dig:
                fim = True
                print("\033[32mParabéns, você acertou a palavra!\033[m")
                time.sleep(2)
            time.sleep(1)
        input("\033[36mPressione Enter para continuar...\033[m")
        os.system("cls")
        cat = input(categorias)
        os.system("cls")
        while not cat.isdigit() or int(cat) > 6 or int(cat) < 1:
            os.system("cls")
            print("\033[31mOpção inválida, tente novamente.\033[m")
            cat = input(categorias)
        cat = int(cat)


    opt = input(menu)
    while not opt.isdigit() or int(opt) > 2 or int(opt) < 1:
      os.system("cls")
      print("\033[31mOpção inválida, tente novamente.\033[m")
      opt = input(menu)

    opt = int(opt)



os.system("cls")
print("\033[31mSaindo...\033[m")
