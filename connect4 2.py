def main():
	import numpy as np
	import pygame
	import sys
	import math
	import menu


	ROW_COUNT = 6
	COLUMN_COUNT = 7
	BLUE = (0, 0 ,230)
	BLACK = (0,0,0)
	RED = (255, 0, 0)
	YELLOW = (255, 255, 0)

	def createBoard():
		board = np.zeros((ROW_COUNT,COLUMN_COUNT))
		return board

	def printBoard(board):
		print(np.flipud(board))

	def isValidLocation(col, board):
		return board[ROW_COUNT-1][col] == 0

	def placePeice(col, board, row, peice):
		board[row][col] = peice

	def getNextRow(col, board):
		for r in range(ROW_COUNT):
			if board[r][col] == 0:
				return r

	def checkIfWon(board, peice):
		#horizontal locations for win
		for c in range(COLUMN_COUNT-3):
			for r in range(ROW_COUNT):
				if board[r][c] == peice and board[r][c+1] == peice and board[r][c+2] == peice and board[r][c+3] == peice:
					return True

		#vertical locations for win
		for c in range(COLUMN_COUNT):
			for r in range(ROW_COUNT-3):
				if board[r][c] == peice and board[r+1][c] == peice and board[r+2][c] == peice and board[r+3][c] == peice:
					return True

		#Check Positive Slope Diagonals
		for c in range(COLUMN_COUNT-3):
			for r in range(ROW_COUNT-3):
				if board[r][c] == peice and board[r+1][c+1] == peice and board[r+2][c+2] == peice and board[r+3][c+3] == peice:
					return True

		#Check Negative Slope Diagonals
		for c in range(COLUMN_COUNT-3):
			for r in range(3, ROW_COUNT):
				if board[r][c] == peice and board[r-1][c+1] == peice and board[r-2][c+2] == peice and board[r-3][c+3] == peice:
					return True

	def drawBoard(board):
		for c in range(COLUMN_COUNT):
			for r in range(ROW_COUNT):
				pygame.draw.rect(screen, BLUE, (c*SQUARE, r*SQUARE+SQUARE, SQUARE, SQUARE))
				pygame.draw.circle(screen, BLACK, (int(c*SQUARE+SQUARE/2), int(r*SQUARE+SQUARE+SQUARE/2)), RADIUS)

		for c in range(COLUMN_COUNT):
			for r in range(ROW_COUNT):		
				if board[r][c] == 1:
					pygame.draw.circle(screen, RED, (int(c*SQUARE+SQUARE/2), height-int(r*SQUARE+SQUARE/2)), RADIUS)
				elif board[r][c] == 2: 
					pygame.draw.circle(screen, YELLOW, (int(c*SQUARE+SQUARE/2), height-int(r*SQUARE+SQUARE/2)), RADIUS)
		pygame.display.update()


	board = createBoard()
	game_over = False
	playerturn = 0


	pygame.init()

	SQUARE = 100
	RADIUS = int(SQUARE/2 - 5)
	width = COLUMN_COUNT * SQUARE
	height = (ROW_COUNT+1) * SQUARE

	size = (width, height)

	screen = pygame.display.set_mode(size)
	drawBoard(board)
	pygame.display.update()
	font = pygame.font.SysFont("monospace", 75)


	while not game_over:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			if event.type == pygame.MOUSEMOTION:
				pygame.draw.rect(screen, BLACK, (0,0,width,SQUARE))
				posx = event.pos[0]
				if playerturn == 0:
						pygame.draw.circle(screen, RED, (posx, int(SQUARE/2)), RADIUS)
				else:
					pygame.draw.circle(screen, YELLOW, (posx, int(SQUARE/2)), RADIUS)
				pygame.display.update()

			if event.type == pygame.MOUSEBUTTONDOWN:
				# print(event.pos)
				pygame.draw.rect(screen, BLACK, (0,0,width,SQUARE))

				if playerturn == 0:
					posx = event.pos[0]
					col = int(math.floor(posx/SQUARE))
					if isValidLocation(col, board):
						row = getNextRow(col, board)
						placePeice(col, board, row, 1)

						if checkIfWon(board, 1):
							print("Player 1 Wins!")
							label = font.render("Player 1 Wins!!!", 1, RED)
							screen.blit(label, (40,10))
							game_over = True

				else:
					posx = event.pos[0]
					col = int(math.floor(posx/SQUARE))
					if isValidLocation(col, board):
						row = getNextRow(col, board)
						placePeice(col, board, row, 2)

						if checkIfWon(board, 2):
							print("Player 2 Wins!")
							label = font.render("Player 2 Wins!!!", 1, YELLOW)
							screen.blit(label, (40,10))
							game_over = True

				printBoard(board)
				drawBoard(board)
				playerturn +=1
				playerturn = playerturn%2


				if game_over:
					pygame.time.wait(3000)
					menu.main()
				



