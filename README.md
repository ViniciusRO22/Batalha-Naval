# Batalha Naval em Python

## Descrição
Este é um jogo simples de **Batalha Naval** implementado em Python. O jogo é baseado em turnos e permite que um jogador dispute contra a inteligência artificial do computador.

## Funcionalidades
- Criar um tabuleiro 10x10 preenchido com água.
- Permitir que o jogador posicione suas embarcações.
- Posicionar aleatoriamente as embarcações do computador.
- Alternar turnos entre o jogador e o computador.
- Exibir o tabuleiro atualizado a cada turno.
- Determinar o vencedor quando todas as embarcações de um dos jogadores forem afundadas.
- Salvar o resultado do jogo em um arquivo `resultado.txt`.

## Dependências
Este jogo requer a biblioteca `numpy` para manipulação dos tabuleiros. Certifique-se de instalá-la antes de executar o programa:

```bash
pip install numpy
```

## Como Jogar
1. Execute o script `main.py`:
   ```bash
   python main.py
   ```
2. Posicione suas embarcações inserindo as coordenadas no formato linha (0-9) e coluna (0-9).
3. O jogo alterna turnos entre você e o computador:
   - Digite as coordenadas para atirar.
   - O computador escolherá coordenadas aleatórias para atacar.
4. O jogo termina quando todas as embarcações de um dos jogadores forem destruídas.
5. O resultado do jogo será salvo no arquivo `resultado.txt`.

## Estrutura do Código
- `criar_tabuleiro()`: Cria um tabuleiro 10x10 preenchido com "Água".
- `mostrar_tabuleiro()`: Exibe o tabuleiro no console.
- `posicionar_embarcacoes_jogador()`: Permite que o jogador posicione 5 embarcações.
- `posicionar_embarcacoes_computador()`: Posiciona 5 embarcações aleatoriamente para o computador.
- `atirar()`: Realiza um tiro e retorna se acertou, errou ou repetiu uma jogada.
- `jogo()`: Controla o fluxo do jogo e alterna os turnos.
- `salvar_resultado()`: Salva o tabuleiro final e o vencedor no arquivo `resultado.txt`.

## Exemplo de Tabuleiro
Durante o jogo, o tabuleiro é exibido assim:
```
  0 1 2 3 4 5 6 7 8 9
0 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
1 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
2 ~ ~ ~ N ~ ~ ~ ~ ~ ~
3 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
4 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
...
```
Os símbolos representam:
- `~`: Água
- `N`: Navio (oculto do adversário)
- `A`: Navio afundado
- `E`: Tiro errado

## Autor
Este jogo foi desenvolvido como um projeto simples para prática de Python e lógica de programação, para as aulas do CEFETMG, pelos alunos Vinícius Ramalho, Lucas Roseno e Hugo Marques 

