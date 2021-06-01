import pygame
import sys


pygame.init()


WINDOW_SIZE = (700, 500)
BACKGROUND_COLOR = (208, 240, 192)

screen = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()
image = pygame.image.load('data/img/character.png')


while True:
    screen.fill(BACKGROUND_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(image, (300, 300))

    pygame.display.flip()
    clock.tick(60)
