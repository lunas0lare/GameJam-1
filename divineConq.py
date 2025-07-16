import pygame

pygame.init()
window = pygame.display.set_mode((1920, 1080))
window.fill((0,0,0))
alcohol_img = pygame.image.load('trash assets/alcohol 1.png')
# window.blit(alcohol_img, (420, 420))
pygame.display.update()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.key.set_repeat()