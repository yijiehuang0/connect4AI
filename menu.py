import pygame
import connect4
import sys

def main():

	def text_objects(text, font):
	    textSurface = font.render(text, True, BLACK)
	    return textSurface, textSurface.get_rect()

	def is_valid_location(x,y,w,h):
		if x+w > mouse[0] > x and y+h > mouse[1] > y:
			return True
		else:
			return False


	WHITE = (255,255,255)
	BLACK = (0,0,0)
	GREEN  = (0,255, 0)
	RED  = (255,0, 0)


	(width, height) = (800, 700)
	screen = pygame.display.set_mode((width, height))
	pygame.display.set_mode((width, height))
	screen.fill(WHITE)
	pygame.display.flip()
	pygame.init()
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()



	font = pygame.font.SysFont("monospace", 90)


	pygame.display.set_caption('Connect Four Game')
	TextSurf, TextRect = text_objects("Play Connect Four", font)
	TextRect.center = ((width/2),(height/3))
	screen.blit(TextSurf, TextRect)



	pygame.draw.rect(screen, GREEN,(150,450,100,50))
	smallText = pygame.font.Font("freesansbold.ttf",20)
	textSurf, textRect = text_objects("Play!", smallText)
	textRect.center = ( (150+(100/2)), (450+(50/2)) )
	screen.blit(textSurf, textRect)
	pygame.display.update()
	startButton = quitButton = pygame.Rect(150,450,100,50)



	pygame.draw.rect(screen, RED,(550,450,100,50))
	smallText = pygame.font.Font("freesansbold.ttf",20)
	textSurf, textRect = text_objects("QUIT!", smallText)
	textRect.center = ( (550+(100/2)), (450+(50/2)) )
	screen.blit(textSurf, textRect)
	pygame.display.update()
	quitButton = pygame.Rect(550,450,100,50)




	running = True
	while running:
	  for event in pygame.event.get():
	    if event.type == pygame.QUIT:
	      	sys.exit()
	    elif event.type == pygame.MOUSEBUTTONDOWN:
	             mouse_pos = event.pos
	             if quitButton.collidepoint(mouse_pos):
	             	sys.exit()
	             if startButton.collidepoint(mouse_pos):
	             	connect4.main()

     	

main()


