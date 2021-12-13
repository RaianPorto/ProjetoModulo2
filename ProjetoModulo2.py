import random

def fimDeJogo():
    print('FIM DE JOGO')
    exit()

def forca(qtdErros):
    if qtdErros == 0:
        print('''
        _ _ _ _ _ _ _ _ _
        | _ _ _ _ _ _ _ _.|
        ||               
        ||             
        ||                    ___
        ||                   |   \  ____  | __  __     \      / º | ___       |  ___
        ||                   |__./ /    \ |/  \/  \     \    /  | |/   \  ___ | /   \ 
        ||                   |   \( ____/ |   |    |     \  /   | |    | /    ||     |
        ||                   |_ _/ \_____ |   |    |      \/    | |    | \___/| \___/
        ||               
        ||                
        ||                 
        ||            
        ||           
        ||           
        ||          
        ||         
        ||        
        ''')
    elif qtdErros == 1:
        print('''
        _ _ _ _ _ _ _ _ _
        | _ _ _ _ _ _ _ _.|
        ||               ___
        ||             (     )
        ||             | o o |
        ||             |_____|
        ||               \ /
        ||           ----------
        ||                      
        ||            |      |   
        ||            |      |    
        ||            |      |     
        ||            |______|
        ||           
        ||           
        ||          
        ||         
        ||        
        ''')
        return False
    elif qtdErros == 2:
        print('''
        _ _ _ _ _ _ _ _ _
        | _ _ _ _ _ _ _ _.|
        ||               ___
        ||             (     )
        ||             | o o |
        ||             |_____|
        ||               \ /
        ||           ----------
        ||         /            
        ||        /  /|      |
        ||       /  / |      |  
        ||      /  /  |      |   
        ||            |______|
        ||            
        ||          
        ||          
        ||         
        ||       
        ''')
        return False
    elif qtdErros == 3:
        print('''
        _ _ _ _ _ _ _ _ _
        | _ _ _ _ _ _ _ _.|
        ||               ___
        ||             (     )
        ||             | o o |
        ||             |_____|
        ||               \ /
        ||           ----------
        ||         /            \ 
        ||        /  /|      |\  \ 
        ||       /  / |      | \  \ 
        ||      /  /  |      |  \  \ 
        ||            |______|
        ||            
        ||           
        ||          
        ||         
        ||        
        ''')
        return False
    elif qtdErros == 4:
        print('''
        _ _ _ _ _ _ _ _ _
        | _ _ _ _ _ _ _ _.|
        ||               ___
        ||             (     )
        ||             | o o |
        ||             |_____|
        ||               \ /
        ||           ----------
        ||         /            \ 
        ||        /  /|      |\  \ 
        ||       /  / |      | \  \ 
        ||      /  /  |      |  \  \ 
        ||            |______|
        ||           /         
        ||          /    / 
        ||         /    /   
        ||        /    /     
        ||       /    /       
        ''')
        return False
    else:
        print('''
        _ _ _ _ _ _ _ _ _
        | _ _ _ _ _ _ _ _.|
        ||               ___
        ||             (     )
        ||             | X X |
        ||             |_____|
        ||               \ /
        ||           ----------
        ||         /            \ 
        ||        /  /|      |\  \ 
        ||       /  / |      | \  \ 
        ||      /  /  |      |  \  \ 
        ||            |______|
        ||           /        \ 
        ||          /    /\    \ 
        ||         /    /  \    \ 
        ||        /    /    \    \ 
        ||       /    /      \    \ 
        ''')
        return True

def converteListaString(lista):
    palavra = ''

    for caracter in lista:
        palavra = palavra + caracter.upper()

    return palavra

def iniciarJogo(palavrasDefinidas):

    qtdErros = 0
    jogadores = []


    for chave, dados in palavrasDefinidas.items():
        montagemDaPalavra = ['_']*len(dados[0])
        palavrasDefinidas[chave].append(montagemDaPalavra)
        palavrasDefinidas[chave].append(qtdErros)
        jogadores.append(chave)

    indice = 0
    qtdJogadores = len(jogadores)
    
    while indice <= qtdJogadores:
        palavraASerEncontrada = palavrasDefinidas[jogadores[indice]][0]
        montagemDaPalavra = palavrasDefinidas[jogadores[indice]][1]

        print(f'{jogadores[indice]}, é sua vez!')

        forca(palavrasDefinidas[jogadores[indice]][2])

        print(converteListaString(palavrasDefinidas[jogadores[indice]][1]))
        print(palavrasDefinidas)
        letraEscolhida = input('Escolha uma letra: ')
        palavraEncontrada = False
        forcaCompleta = False

        while letraEscolhida in palavraASerEncontrada or palavraEncontrada == True or forcaCompleta == True:
            
            for pos, letra in enumerate(palavraASerEncontrada):
                if letraEscolhida == palavraASerEncontrada[pos]:
                    montagemDaPalavra[pos] = letraEscolhida

            forca(palavrasDefinidas[jogadores[indice]][2])
            print(converteListaString(palavrasDefinidas[jogadores[indice]][1]))
            situacaoDaPalavra = "".join(palavrasDefinidas[jogadores[indice]][1])
            if palavrasDefinidas[jogadores[indice]][0] == situacaoDaPalavra:
                print(f'Parabens, {jogadores[indice]}, você ganhou! Você encontrou a palavra antes dos outros jogadores e antes de se enforcar!')
                fimDeJogo()
            else:
                letraEscolhida = input('Escolha outra letra: ')
        
        palavrasDefinidas[jogadores[indice]][1] = montagemDaPalavra
        palavrasDefinidas[jogadores[indice]][2] += 1

        if palavrasDefinidas[jogadores[indice]][2] >= 5:
            print('VOCÊ SE ENFORCOU!')
            forca(palavrasDefinidas[jogadores[indice]][2])
            forcaCompleta = forca(palavrasDefinidas[jogadores[indice]][2])
            print(palavrasDefinidas)
        else:
            print('Você Errou!')
            print('passe a vez para o próximo jogador!')

        if indice == qtdJogadores-1:
            indice = 0
        else:
            indice += 1

def atribuirPalavras(nivel, jogadores):
    palavrasEscolhidas = []
    palavrasFaceis = ['banana', 'arroz', 'batata', 'maçã', 'pizza', 'queijo', 'goiaba', 'feijao', 'bife', 'frango', 'sushi', 'jaca', 'açai', 'alface', 'amora', 'aipim', 'empada', 'paçoca', 'tacos', 'vagem']
    palavrasNormais = ['televisor', 'monitor', 'grill', 'freezer', 'microondas', 'fritadeira', 'sanduicheira', 'liquidificador', 'bebedouro', 'cafeteira', 'torradeira', 'batedeira', 'tanquinho', 'refrigerador', 'lavadora', 'cooktop', 'projetor', 'aspirador', 'lava-louças', 'secador']
    palavrasDificeis = ['indentação', 'algoritimização', 'back-end', 'comitar', 'debugger', 'framework', 'funfar', 'full-stack', 'refatoração', 'overflow', 'interpreter', 'prompt', 'branch', 'checkout', 'query', 'socket', 'bootstrap', 'jquery', 'middleware', 'backlog']

    # print(nivel)

    
    # print(dir(jogadores))

    for chave, dados in jogadores.items():
        # print(dados)
        
        if nivel == 1:
            dados.append(random.choice(palavrasFaceis))
        elif nivel == 2:
            dados.append(random.choice(palavrasNormais))
        elif nivel == 3:
            dados.append(random.choice(palavrasDificeis))

        # print(jogadores)
    return jogadores

def escolherNivel():
    print('''
    1 - Nível Fácil
    2 - Nivel Normal
    3 - Nivel Difícil
    0 - Voltar para o modo de jogo
    ''')
    
    escolhaDeNivel = int(input('Escolha o nível que querem jogar: '))

    if escolhaDeNivel == 0:
        modoDeJogoMultiplayer()
    elif escolhaDeNivel == 1 or escolhaDeNivel == 2 or escolhaDeNivel == 3:
        return escolhaDeNivel
    else:
        escolherNivel()
    
def modoDeJogoSolo():
    print('')

def modoDeJogoMultiplayer():
    print('')
    qtdJogadores = int(input('Quantos jogadores irão participar? '))

    jogadores = {}

    if qtdJogadores > 1:
        for n in range(1, qtdJogadores+1):
            # id = input(f'Informe o ID do {n}º/ª jogador(a)? ')
            nome = input(f'Qual o nome do {n}º/ª jogador(a)? ')
            chave = nome
            jogadores[chave] = []
    else:
        print('Só é permitido jogar com 2(dois) ou mais jogadores!')
        modoDeJogoMultiplayer()

    nivelEscolhido = escolherNivel()
    palavrasDefinidas = atribuirPalavras(nivelEscolhido, jogadores)
    iniciarJogo(palavrasDefinidas)

def modoMesaEJogador():
    print('')

def subMenuIniciarjogo():

    print('''
    SUBMENU INICIAR JOGO

    1 - Modo Solo
    2 - Modo Multiplayer
    3 - Modo Mesa e Jogador
    0 - Voltar para o Menu Principal
    ''')

    escolha = int(input('Escolha uma opção: '))

    if escolha == 0:
        menuPrincipal()
    elif escolha == 1:
        modoDeJogoSolo()
    elif escolha == 2:
        modoDeJogoMultiplayer()
    elif escolha == 3:
        modoMesaEJogador()
    else:
        print('Opção invalida! Escolha uma opção válida!')
        subMenuIniciarjogo()

def sobreOJogo():
    print('Sobre o jogo!')

def sobreOProjeto():
    print('SOBRE O PROJETO')

def finalizarJogo():
    print('Finalizando jogo . . .')
    print('JOGO FINALIZADO!')

def menuPrincipal():
    print('Bem Vindo ao jogo da forca!')
    print('''
    MENU

    1 - Iniciar Jogo
    2 - Sobre o Jogo
    3 - Sobre o Projeto
    0 - Sair do Jogo

    ''')

    escolha = int(input('Escolha uma opção: '))

    if escolha == 0:
        finalizarJogo()
    elif escolha == 1:
        subMenuIniciarjogo()
    elif escolha == 2:
        sobreOJogo()
    elif escolha == 3:
        sobreOProjeto()
    else:
        print('Opção invalida! Escolha uma opção válida!')
        menuPrincipal()

forca(qtdErros=0)
menuPrincipal()