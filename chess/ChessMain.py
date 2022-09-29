"""
Este é o arquivo de driver principal. Ele ficará responsável por gerenciar input do usuário e disponibilizar o GameState object atual.
"""

import pygame as p
import ChessEngine

WIDTH = HEIGHT = 512 #400 é outra opção.
DIMENSION = 8 #dimensões de um tabuleiro de xadrez é de 8x8.
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15 #para animações no futuro.
IMAGES = {}

'''
Inicializar um dicionário global de imagens. Isto será chamado exatamente uma única vez no main.
'''
def loadImages():
	pieces = ['bP', 'bT', 'bC', 'bB', 'bK', 'bQ','pP', 'pT', 'pC', 'pB', 'pK', 'pQ']
	for piece in pieces:
		IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))
	#Nota: nós podemos acessar uma imagem ao dizer 'IMAGES['bP']'

'''
O driver principal para nosso código. Isto irá gerenciar o input do usuário e atualizar os gráficos.
'''
def main():
	p.init()
	screen = p.display.set_mode((WIDTH, HEIGHT))
	clock = p.time.Clock()
	screen.fill(p.Color("white"))
	gs = ChessEngine.GameState()
	print(gs.board)
	loadImages() #fazer isso só uma vez, antes do loop while
	running = True
	while running:
		for e in p.event.get():
			if e.type == p.QUIT:
				running = False
		drawGameState(screen, gs)
		clock.tick(MAX_FPS)
		p.display.flip()

'''
Responsável por todos os gráficos dentro de um game state atual.
'''
def drawGameState(screen, gs):
	drawBoard(screen) #desenha quadrados no tabuleiro
	#adicionar foco nas peças ou sugestões de movimentos (futuro)
	drawPieces(screen, gs.board) #desenhar peças em cima destes quadrados

'''
Desenha os quadrados no tabuleiro. O quadrado no canto superior esquerdo é sempre claro.
'''
def drawBoard(screen):
	colors = [p.Color(255,255,255), p.Color(255,128,0)]
	for r in range(DIMENSION):
		for c in range(DIMENSION):
			color = colors[((r+c)%2)]
			p.draw.rect(screen, color, p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

'''
Desenha as peças no tabuleiro utilizando o GameState.board atual
'''
def drawPieces(screen, board):
	for r in range(DIMENSION):
		for c in range(DIMENSION):
			piece = board[r][c]
			if piece != "--": #não é um quadrado vazio
				screen.blit(IMAGES[piece], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

if __name__ == "__main__":
	main()