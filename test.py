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
        self.location.x = Movement.x
        self.location.y = Movement.y

def update_Score():
    global score
    score += 1   

class handling_things():
    def __init__(self):
        pass
    def handle_collision(self, me: unit, mob: unit) -> Vector2:
        if(me.rect.colliderect(mob.rect) == True):
            update_Score()
           
            return Vector2(randint(0, 700), randint(0, 500))
            
        return mob.location
    
class Game():
    
    def __init__(self):
        pygame.init()
        #text font
        self.text_font = pygame.font.Font('Pixeltype.ttf', 50)
        #creating score
        self.score = 0
        #frame per second
        self.FPS = 10
        #movement speed of object
        self.meMovementSpeed = 6
        self.modMovementSpeed = 2

        global windowPos 
        global score
        score = 0

        windowPos = Vector2(736, 523)
       
        
        self.handle_object = handling_things()

        self.window = pygame.display.set_mode(windowPos)

        #loading background 
        self.backgound_1 = pygame.image.load('background/109th update_ Metropolis 28_?.jpg').convert_alpha()

        #loading object
        self.main = pygame.image.load('trash assets/recycling 2.png').convert_alpha()
        self.mob = pygame.image.load('trash assets/box tile 32X32 4.png').convert_alpha()

       
        #displaying game
        pygame.display.set_caption("TrashCanDoIt")
        self.clock = pygame.time.Clock()

        #creating movement variables
        self.mobsMovement = Vector2(0,0)
        self.meMovement = Vector2(0,0)

        #render background
        self.window.blit(self.backgound_1, (0,0))
        #creating rectangle for collision and rendering
        
        self.meLocation = pygame.math.Vector2(500, 300)
        self.me_rect = self.window.blit(self.main, self.meLocation)#location of me object x = y = 500
       
        self.mobLocation = pygame.math.Vector2(500, 400)
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
        
        mobsMovement = self.handle_object.handle_collision(self.unit[0], self.unit[1])
        self.unit[1].move(mobsMovement)
       
        
    def render(self):

        #fill window color and background
        self.window.fill((0,0,0))
        self.window.blit(self.backgound_1, (0,0))
        
        #render and displaying score
        self.text_surface = self.text_font.render(f'{score}', False, 'white')
        self.window.blit(self.text_surface, (5, 5))
        
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