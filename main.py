import pygame
import os
from pygame.math import Vector2
from sys import exit
from random import randint
import asyncio
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
            
        elif self.rect.topright[0] == windowPos.x:
            self.location.x = windowPos.x - 20
        if(self.location.y < 0):
            self.location.y = 0
        elif self.rect.bottomleft[1] == windowPos.y:
            self.location.y = windowPos.y - 27
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
        self.sound = pygame.mixer.Sound('retro-coin-1-236677.ogg')
    def handle_collision(self, me: unit, mob: unit) -> Vector2:
        if(me.rect.colliderect(mob.rect) == True):
            update_Score()
            self.sound.play()
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

        #creating countdown
        self.countdown_value = 31
        
        #random mobs's location
        
        global windowPos 
        global score
        score = 0

        windowPos = Vector2(736, 523)
       
        
        self.handle_object = handling_things()

        self.window = pygame.display.set_mode(windowPos)

        #loading game over screen
        self.gameover_screen = pygame.image.load('game_over.jpg').convert_alpha()
        #loading background 
        self.backgound_1 = pygame.image.load('background/109th update_ Metropolis 28_?.jpg').convert_alpha()

        #loading object
        self.main = pygame.image.load('trash assets/recycling 2.png').convert_alpha()

        self.mob1 = pygame.image.load('trash assets/box tile 16x16 1.png').convert_alpha()
        self.mob2 = pygame.image.load('trash assets/box tile 16x16 4.png').convert_alpha()
        self.mob3 = pygame.image.load('trash assets/box tile 16x16 5.png').convert_alpha()
       
        self.mob_list = [self.mob1, self.mob2, self.mob3]
        #displaying game
        pygame.display.set_caption("TrashCanDoIt")
        self.clock = pygame.time.Clock()

        #creating movement variables
        # self.mobsMovement = Vector2(0,0)
        self.meMovement = Vector2(0,0)

        #render background
        self.window.blit(self.backgound_1, (0,0))
        #creating rectangle for collision and rendering
        
        self.meLocation = pygame.math.Vector2(165, 350)
        self.me_rect = self.window.blit(self.main, self.meLocation)#location of me object x = y = 500
        
        self.mobLocation_1 = pygame.math.Vector2(randint(0, 700), randint(0, 500))
        self.mobLocation_2 = pygame.math.Vector2(randint(0, 700), randint(0, 500))
        self.mobLocation_3 = pygame.math.Vector2(randint(0, 700), randint(0, 500))
        self.mob_rect_1 = self.window.blit(self.mob1, self.mobLocation_1)
        self.mob_rect_2 = self.window.blit(self.mob2, self.mobLocation_2)
        self.mob_rect_3 = self.window.blit(self.mob3, self.mobLocation_3)

        self.unit = [
            mob(self.mobLocation_1, self.mob_rect_1),
            mob(self.mobLocation_2, self.mob_rect_2),
            mob(self.mobLocation_3, self.mob_rect_3)
                     ]
        self.me = me(self.meLocation, self.me_rect)
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
        self.me.move(self.meMovement)#when convert into vector, only need to truyen vao class
        
        for mob in self.unit:
            mobsMovement = self.handle_object.handle_collision(self.me, mob)
            mob.move(mobsMovement)
       
        
    def render(self):
        #fill window color and background
        self.finish = True
        
        if(self.finish != False):
            self.window.fill((0,0,0))
            self.window.blit(self.backgound_1, (0,0))
            
            #render countdown
            self.countdown = int(self.countdown_value - pygame.time.get_ticks() / 1000)
            self.countdown_surface = self.text_font.render(f'{self.countdown}', False, 'yellow')
            self.window.blit(self.countdown_surface, (700, 5))
            
            #render and displaying score
            self.text_surface = self.text_font.render(f'{score}pt', False, 'white')
            self.window.blit(self.text_surface, (5, 5))
            
            self.me_rect = self.window.blit(self.main, (self.me.location.x, self.me.location.y))
            self.me.rect = self.me_rect

            temp = 0
            for mob in self.mob_list:
                self.mob_rect = self.window.blit(mob, (self.unit[temp].location.x, self.unit[temp].location.y))
                self.unit[temp].rect = self.mob_rect
                temp = temp + 1
            if(self.countdown <= 0):
                self.finish = False
        if(self.finish == False):
            self.window.blit(self.gameover_screen, (-130, -230)) 
            self.window.blit(self.text_font.render('your score: ' + f'{score}', False, 'black'), (230, 450))
           
           
        pygame.display.update()
        
    def run(self):
        
        while self.running:
            self.processInput()
            self.update()
            self.render()
            self.clock.tick(60)

    async def run_async(self):
        while self.running:
            self.processInput()
            self.update()
            self.render()
            self.clock.tick(60)
            await asyncio.sleep(0)  
            
async def main():
    game = Game()
    await game.run_async()
    pygame.quit()
    

asyncio.run(main())