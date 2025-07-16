import pygame
import os
from pygame.math import Vector2
from sys import exit
from random import randint
os.environ['SDL_VIDEO_CENTERED'] = '1'

class unit():
    def __init__(self, state, pos, rect):
        self.state = state
        self.pos = pos
        self.rect = rect
    def move(self, Movement):
        raise NotImplementedError()
    
class me(unit):
    def __init__(self, rect):
       state = gameState()
       pos = state.pos
       super().__init__(state, pos, rect)
    
    def move(self, Movement):
        if(self.pos.x < 0):
            self.pos.x = 0
        elif self.pos.x > self.windowPos.x:
            self.pos.x = self.windowPos.x - self.meSize.x

        if(self.pos.y < 0):
            self.pos.y = 0
        elif self.pos.y > self.windowPos.y:
            self.pos.y = self.windowPos.y - self.meSize.y
        self.pos.x += Movement.x
        self.pos.y += Movement.y
        
class mob(unit):
    def __init__(self, rect):
       state = gameState()
       pos = state.pos
       super().__init__(state, pos, rect)
    
    def move(self, Movement):
        
    # self.mobs_movement.x += self.modMovementSpeed
        if(self.gameState.handleCollision(self.me_rect, self.mob_rect) == True):
            self.mobs_movement.y = randint(0, 100)

class gameState():
    def __init__(self):
        self.pos = Vector2(240, 240)
        #put create window here, use vector(x, y)(this is a class)
        self.windowPos = Vector2(1000, 800)
        
        self.meSize = Vector2(28,16)
    def update(self, Movement):
        for unit in self.units:
        me.move(self, Movement)
        
    def handleCollision(self, main_rect, mob_rect):
        if(main_rect.colliderect(mob_rect)):
            return True

class Game():
    def __init__(self):
        #frame per second
        self.FPS = 10
        #movement speed of object
        self.meMovementSpeed = 6
        self.modMovementSpeed = 2
        pygame.init()
        self.gameState = gameState()

        self.window = pygame.display.set_mode(self.gameState.windowPos)

        #loading object
        self.main = pygame.image.load('trash assets/box 1.png').convert_alpha()
        self.mob = pygame.image.load('trash assets/recycling 1.png').convert_alpha()

        #displaying game
        pygame.display.set_caption("TrashCanDoIt")
        self.clock = pygame.time.Clock()

        #creating movement variables
        self.mobs_movement = Vector2(0,0)
        self.meMovement = Vector2(0,0)

        #creating rectangle for collision and rendering
        self.meLocation = pygame.math.Vector2(500, 500)
        self.me_rect = self.window.blit(self.main, self.meLocation)#location of me object x = y = 500

        self.mobLocation = pygame.math.Vector2(500, 700)
        self.mob_rect = self.window.blit(self.mob, self.mobLocation)

        self.running = True
    
    def processInput(self):
        self.meMovement = Vector2(0,0)
        
        for event in pygame.event.get():
            pygame.key.set_repeat(1, self.FPS)
            if event.type == pygame.QUIT:
                self.running = False
                exit()
                
            elif event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    break
                elif event.key == pygame.K_RIGHT:
                    self.meMovement.x = self.meMovementSpeed
                elif event.key == pygame.K_LEFT:
                    self.meMovement.x = -self.meMovementSpeed
                elif event.key == pygame.K_DOWN:
                    self.meMovement.y = self.meMovementSpeed
                elif event.key == pygame.K_UP:
                    self.meMovement.y = -self.meMovementSpeed
                    
    def update(self):
        self.gameState.update(self.meMovement)#when convert into vector, only need to truyen vao class
        self.mobs_movement.x += self.modMovementSpeed

    def render(self):
        self.window.fill((0,0,0))
        x = self.gameState.pos.x
        y = self.gameState.pos.y
        self.location = pygame.math.Vector2(x, y)

        self.me_rect = self.window.blit(self.main, self.location)
        
        self.mob_rect = self.window.blit(self.mob, pygame.math.Vector2(self.mobs_movement.x, self.mobs_movement.y))
        
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