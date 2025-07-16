import pygame
import os
from pygame.math import Vector2
os.environ['SDL_VIDEO_CENTERED'] = '1'

class gameState():
    def __init__(self):
        self.mePos = Vector2(240, 240)
        #put create window here, use vector(x, y)(this is a class)
        self.windowPos = Vector2(1000, 800)
        
        self.meSize = Vector2(28,16)
    def update(self, Movement):
        if(self.mePos.x < 0):
            self.mePos.x = 0
        elif self.mePos.x > self.windowPos.x:
            self.mePos.x = self.windowPos.x - self.meSize.x

        a = self.windowPos.y - self.meSize.y
        if(self.mePos.y < 0):
            self.mePos.y = 0
        elif self.mePos.y > self.windowPos.y:
            self.mePos.y = a
        self.mePos.x += Movement.x
        self.mePos.y += Movement.y


class Game():
    def __init__(self):
        self.moveSpeed = 10
        pygame.init()
        self.gameState = gameState()

        self.window = pygame.display.set_mode(self.gameState.windowPos)

        self.main = pygame.image.load('trash assets/box 1.png')
        self.mob = pygame.image.load('trash assets/recycling 1.png')

        pygame.display.set_caption("TrashCanDoIt")
        self.clock = pygame.time.Clock()

        self.mobs_movement = Vector2(0,0)
        self.meMovement = Vector2(0,0)
        self.running = True
    
    def processInput(self):
        self.meMovement = Vector2(0,0)
        
        for event in pygame.event.get():
            pygame.key.set_repeat(1, self.moveSpeed)
            if event.type == pygame.QUIT:
                self.running = False
                break
                
            elif event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    break
                elif event.key == pygame.K_RIGHT:
                    self.meMovement.x = 10
                elif event.key == pygame.K_LEFT:
                    self.meMovement.x = -10
                elif event.key == pygame.K_DOWN:
                    self.meMovement.y = 10
                elif event.key == pygame.K_UP:
                    self.meMovement.y = -10
                    
    def update(self):
        self.gameState.update(self.meMovement)#when convert into vector, only need to truyen vao class

    def render(self):
        self.window.fill((0,0,0))
        x = self.gameState.mePos.x
        y = self.gameState.mePos.y
        self.location = pygame.math.Vector2(x, y)
        self.window.blit(self.main, self.location)
        self.mobs_movement.x += 5
        self.window.blit(self.mob, pygame.math.Vector2(self.mobs_movement.x, self.mobs_movement.y))
        pygame.display.update()
        
    def run(self):
        while self.running:
            self.processInput()
            self.update()
            self.render()
            self.clock.tick(60)

game = Game()
game.run()
pygame.quit()