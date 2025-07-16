import pygame
from sys import exit
unitsTexture = pygame.image.load('trash assets/box 3 dynamic.png')
window = pygame.display.set_mode((256,256))
location = pygame.math.Vector2(96, 96)
# rectangle = pygame.Rect(64, 0, 64, 64)
window.blit(unitsTexture,location)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        pygame.display.update()    

