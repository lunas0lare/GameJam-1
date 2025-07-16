import pygame
import os
from pygame.math import Vector2
os.environ['SDL_VIDEO_CENTERED'] = '1'

class gameState():
    def __init__(self):
        self.tankPos = #this also
        #put create window here, use vector(x, y)(this is a class)
    def update(self, moveCommandX, moveCommandY):
        self.x += moveCommandX
        self.y += moveCommandY


class Game():
    def __init__(self):
        self.moveSpeed = 10
        pygame.init()
        self.gameState = gameState()
        self.window = pygame.display.set_mode((1920, 1080))#move up gamestate
        self.unit = pygame.image.load('trash assets/box 1.png')
        pygame.display.set_caption("Discover Python & Patterns - https://www.patternsgameprog.com")
        self.clock = pygame.time.Clock()
        self.moveCommandX = 0
        self.moveCommandY = 0

        self.running = True
    
    def processInput(self):
        self.moveCommandX = 0
        self.moveCommandY = 0#convert into vector
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
                    self.moveCommandX = 10
                elif event.key == pygame.K_LEFT:
                    self.moveCommandX = -10
                elif event.key == pygame.K_DOWN:
                    self.moveCommandY = 10
                elif event.key == pygame.K_UP:
                    self.moveCommandY = -10
                    
    def update(self):
       self.gameState.update(self.moveCommandX, self.moveCommandY)#when convert into vector, only need to truyen vao class

    def render(self):
        self.window.fill((0,0,0))
        x = self.gameState.x
        y = self.gameState.y
        self.location = pygame.math.Vector2(self.gameState.x, self.gameState.y)
        self.window.blit(self.unit, pygame.math.Vector2(x, y))
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