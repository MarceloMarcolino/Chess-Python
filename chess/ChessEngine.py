"""
Esta é a classe responsável por guardar toda a informação sobre o estado atual de uma partida de xadrez. Ele também será responsável por determinar os movimentos válidos no estado atual. Ele também irá registrar um log de movimentos.
"""
class GameState():
	def __init__(self):
		#tabuleiro é uma lista 2d de 8x8, cada elemento da lista tem 2 caracteres.
		#O primeiro caractere representa a cor da peça, 'p' para preta ou 'b' para branca.
		#O segundo caractere representa o tipo da peça, 'K' para rei, 'Q' para rainha, 'T' para torre, 'B' para bispo, 'C' para cavalo ou 'P' para peão.
		#"--" - representa um espaço vazio sem preças.
		self.board = [
			["pT", "pC", "pB", "pQ", "pK", "pB", "pC", "pT"],
			["pP", "pP", "pP", "pP", "pP", "pP", "pP", "pP"],
			["--", "--", "--", "--", "--", "--", "--", "--"],
			["--", "--", "--", "--", "--", "--", "--", "--"],
			["--", "--", "--", "--", "--", "--", "--", "--"],
			["--", "--", "--", "--", "--", "--", "--", "--"],
			["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
			["bT", "bC", "bB", "bQ", "bK", "bB", "bC", "bT"]]
		self.whiteToMove = True
		self.moveLog = []