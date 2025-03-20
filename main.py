# Importação das bibliotecas necessárias
import numpy as np
import random

def criar_tabuleiro():
    """
    Cria um tabuleiro 10x10 preenchido com "Água"
    Retorna: Array numpy 10x10
    """
    return np.full((10, 10), "Água", dtype=object)

def mostrar_tabuleiro(tabuleiro, revelar_embarcacoes=False):
    """
    Exibe o tabuleiro no console
    Parâmetros:
        tabuleiro: Array numpy 10x10
        revelar_embarcacoes: Boolean - Se True, mostra posição dos navios
    """
    print("  0 1 2 3 4 5 6 7 8 9")  # Números das colunas
    for i in range(10):
        linha = f"{i} "  # Número da linha
        for j in range(10):
            # Mostra '~' para água ou navios escondidos
            if tabuleiro[i][j] == "Água" or (tabuleiro[i][j] == "Navio" and not revelar_embarcacoes):
                linha += "~ "
            else:
                # Mostra primeira letra do status (A)fundado ou (E)rrou
                linha += tabuleiro[i][j][0] + " "
        print(linha)

def posicionar_embarcacoes_jogador(tabuleiro):
    """
    Permite ao jogador posicionar 5 embarcações no tabuleiro
    Parâmetros:
        tabuleiro: Array numpy 10x10
    """
    embarcacoes = 0
    while embarcacoes < 5:
        print(f"\nPosicione a embarcação {embarcacoes + 1}/5:")
        mostrar_tabuleiro(tabuleiro, True)
        try:
            # Solicita coordenadas ao jogador
            x = int(input("Digite a linha (0-9): "))
            y = int(input("Digite a coluna (0-9): "))
            # Verifica se as coordenadas são válidas
            if x < 0 or x > 9 or y < 0 or y > 9:
                print("Coordenadas fora do tabuleiro. Tente novamente.")
                continue
            # Verifica se já existe navio na posição
            if tabuleiro[x, y] == "Navio":
                print("Já existe uma embarcação nesta posição. Tente novamente.")
                continue
            # Posiciona o navio se a posição estiver livre
            if tabuleiro[x, y] == "Água":
                tabuleiro[x, y] = "Navio"
                embarcacoes += 1
        except ValueError:
            print("Entrada inválida. Tente novamente.")
            continue

def posicionar_embarcacoes_computador(tabuleiro):
    """
    Posiciona 5 embarcações aleatoriamente no tabuleiro do computador
    Parâmetros:
        tabuleiro: Array numpy 10x10
    """
    embarcacoes = 0
    while embarcacoes < 5:
        # Gera coordenadas aleatórias
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        # Posiciona o navio se a posição estiver livre
        if tabuleiro[x, y] == "Água":
            tabuleiro[x, y] = "Navio"
            embarcacoes += 1

def atirar(tabuleiro, x, y):
    """
    Realiza um tiro em uma posição do tabuleiro
    Parâmetros:
        tabuleiro: Array numpy 10x10
        x, y: Coordenadas do tiro
    Retorna:
        True se acertou um navio
        False se errou (acertou água)
        None se posição já foi atingida
    """
    if tabuleiro[x, y] == "Navio":
        tabuleiro[x, y] = "Afundada"
        return True
    elif tabuleiro[x, y] == "Água":
        tabuleiro[x, y] = "Errou"
        return False
    return None

def jogo():
    """
    Função principal que controla o fluxo do jogo:
    - Cria tabuleiros
    - Posiciona embarcações
    - Alterna turnos entre jogador e computador
    - Verifica condições de vitória
    """
    # Inicialização dos tabuleiros
    tabuleiro_jogador = criar_tabuleiro()
    tabuleiro_computador = criar_tabuleiro()

    # Posicionamento das embarcações
    posicionar_embarcacoes_jogador(tabuleiro_jogador)
    posicionar_embarcacoes_computador(tabuleiro_computador)

    while True:
        # Turno do jogador
        jogador_continua = True
        while jogador_continua:
            print("\nSeu tabuleiro:")
            mostrar_tabuleiro(tabuleiro_jogador, True)
            print("\nTabuleiro do computador:")
            mostrar_tabuleiro(tabuleiro_computador)

            # Jogador atira
            try:
                entrada = input("Digite a linha para atirar (0-9) ou 'revelar' para ver as embarcações: ")
                # Comando especial para revelar navios do computador
                if entrada.lower() == "revelar":
                    print("\nTabuleiro do computador (revelado):")
                    mostrar_tabuleiro(tabuleiro_computador, True)
                    continue
                
                # Processa as coordenadas do tiro
                x = int(entrada)
                y = int(input("Digite a coluna para atirar (0-9): "))
                # Verifica se as coordenadas são válidas
                if x < 0 or x > 9 or y < 0 or y > 9:
                    print("Coordenadas fora do tabuleiro. Tente novamente.")
                    continue
                # Verifica se a posição já foi atingida
                if tabuleiro_computador[x, y] == "Afundada" or tabuleiro_computador[x, y] == "Errou":
                    print("Você já atirou nesta posição. Tente novamente.")
                    continue
            except ValueError:
                if entrada.lower() != "revelar":
                    print("Entrada inválida. Tente novamente.")
                continue

            # Processa o resultado do tiro
            acertou = atirar(tabuleiro_computador, x, y)
            if acertou:
                print("Você acertou uma embarcação! Ganhou mais um tiro!")
                jogador_continua = True
            else:
                print("Você errou.")
                jogador_continua = False

            # Verifica se o jogador venceu
            if np.count_nonzero(tabuleiro_computador == "Navio") == 0:
                print("Você venceu!")
                salvar_resultado(tabuleiro_jogador, tabuleiro_computador, "jogador")
                return

        # Turno do computador
        computador_continua = True
        while computador_continua:
            # Gera coordenadas aleatórias para o tiro
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            # Verifica se a posição já foi atingida
            if tabuleiro_jogador[x, y] == "Afundada" or tabuleiro_jogador[x, y] == "Errou":
                continue
            
            # Processa o resultado do tiro
            acertou = atirar(tabuleiro_jogador, x, y)
            if acertou:
                print(f"O computador acertou uma embarcação em ({x}, {y})! Ele atirará novamente!")
                computador_continua = True
            else:
                print(f"O computador errou em ({x}, {y}).")
                computador_continua = False
            
            # Verifica se o computador venceu
            if np.count_nonzero(tabuleiro_jogador == "Navio") == 0:
                print("O computador venceu!")
                salvar_resultado(tabuleiro_jogador, tabuleiro_computador, "computador")
                return

def salvar_resultado(tabuleiro_jogador, tabuleiro_computador, vencedor):
    """
    Salva o resultado do jogo em um arquivo texto
    Parâmetros:
        tabuleiro_jogador: Array numpy 10x10
        tabuleiro_computador: Array numpy 10x10
        vencedor: String - "jogador" ou "computador"
    """
    with open("resultado.txt", "w") as arquivo:
        # Escreve o cabeçalho
        arquivo.write(f"RESULTADO DO JOGO - Vencedor: {vencedor.upper()}\n\n")
        
        # Salva o tabuleiro do jogador
        arquivo.write("Tabuleiro do Jogador:\n")
        arquivo.write("  0 1 2 3 4 5 6 7 8 9\n")
        for i in range(10):
            linha = f"{i} "
            for j in range(10):
                if tabuleiro_jogador[i][j] == "Água":
                    linha += "~ "
                else:
                    linha += tabuleiro_jogador[i][j][0] + " "
            arquivo.write(linha + "\n")
        
        # Adiciona uma linha em branco entre os tabuleiros
        arquivo.write("\n")
        
        # Salva o tabuleiro do computador
        arquivo.write("Tabuleiro do Computador:\n")
        arquivo.write("  0 1 2 3 4 5 6 7 8 9\n")
        for i in range(10):
            linha = f"{i} "
            for j in range(10):
                if tabuleiro_computador[i][j] == "Água":
                    linha += "~ "
                else:
                    linha += tabuleiro_computador[i][j][0] + " "
            arquivo.write(linha + "\n")

# Ponto de entrada do programa
if __name__ == "__main__":
    jogo()