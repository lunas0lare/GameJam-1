import pygame
import os
from pygame.math import Vector2
from sys import exit
from random import randint
os.environ['SDL_VIDEO_CENTERED'] = '1'

class unit():
    def __init__(self, location, rect):
        self.location = location
        self.rect = rect
    def move(self, Movement):
        raise NotImplementedError()
    
class me(unit):
    def __init__(self, location, rect):
       super().__init__(location, rect)
    
    def move(self, Movement):
        if(self.location.x < 0):
            self.location.x = 0
            
        elif self.location.x > windowPos.x:
            self.location.x = windowPos.x - self.rect.width

        if(self.location.y < 0):
            self.location.y = 0
        elif self.location.y > windowPos.y:
            self.location.y = windowPos.y - self.rect.height
        self.location.x += Movement.x
        self.location.y += Movement.y
        
class mob(unit):
    def __init__(self,location, rect):
       super().__init__(location, rect)
    
    def move(self, Movement: int):
        self.location.y += Movement
        

class handling_things():
    def __init__(self):
        pass
    def handle_collision(self, me: unit, mob: unit):
        if(me.rect.colliderect(mob.rect) == True):
            mob.move(randint(-100, 100))


class Game():
    
    def __init__(self):
        #frame per second
        self.FPS = 10
        #movement speed of object
        self.meMovementSpeed = 6
        self.modMovementSpeed = 2

        global windowPos 
        windowPos = Vector2(1080, 800)
        pygame.init()
        
        self.handle_object = handling_things()

        self.window = pygame.display.set_mode(windowPos)

        #loading object
        self.main = pygame.image.load('trash assets/box 1.png').convert_alpha()
        self.mob = pygame.image.load('trash assets/recycling 1.png').convert_alpha()

        #displaying game
        pygame.display.set_caption("TrashCanDoIt")
        self.clock = pygame.time.Clock()

        #creating movement variables
        self.mobsMovement = Vector2(0,0)
        self.meMovement = Vector2(0,0)

        #creating rectangle for collision and rendering
        
        self.meLocation = pygame.math.Vector2(500, 500)
        self.me_rect = self.window.blit(self.main, self.meLocation)#location of me object x = y = 500

        self.mobLocation = pygame.math.Vector2(700, 400)
        self.mob_rect = self.window.blit(self.mob, self.mobLocation)
        
        self.unit = [
            me(self.meLocation, self.me_rect),
            mob(self.mobLocation, self.mob_rect)
                     ]
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
        self.unit[0].move(self.meMovement)#when convert into vector, only need to truyen vao class
        # self.mobsMovement.y = 1
        self.handle_object.handle_collision(self.unit[0], self.unit[1])

    def render(self):
        self.window.fill((0,0,0))

        self.me_rect = self.window.blit(self.main, (self.unit[0].location.x, self.unit[0].location.y))
        self.unit[0].rect = self.me_rect
        self.mob_rect = self.window.blit(self.mob, (self.unit[1].location.x, self.unit[1].location.y))
        self.unit[1].rect = self.mob_rect
       
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