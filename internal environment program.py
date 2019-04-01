import pygame
import os
import time
import random
pygame.init() #starts pygame
img_path = os.path.join('C:\Python34', 'trash.png') #where each sprite image is loaded from in the computer
img_path1 = os.path.join('C:\Python34', 'rubbish.png')
display_width = 500
display_height = 750
white = (255,255,255)
clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode((display_width, display_height)) #sets size of gameDisplay/window in pixels

class Trash(object):  # represents the trashcan, not the game
    def __init__(self):
        self.image = pygame.image.load(img_path)
        # the trashcans's position
        self.x = 0
        self.y = 0
    def handle_keys(self):
        """ Handles Keys """
        key = pygame.key.get_pressed()
        dist = 1 # distance moved in 1 frame, try changing it to 5
        if key[pygame.K_DOWN] and self.y < 1400 - display_height-dist: # down key
            self.y += dist # move down
        elif key[pygame.K_UP] and self.y>dist: # up key
            self.y -= dist # move up
        if key[pygame.K_RIGHT] and self.x < 950 - display_width-dist: # right key
            self.x += dist # move right
        elif key[pygame.K_LEFT] and self.x>dist: # left key
            self.x -= dist #move left
            
            
            

    def draw(self, surface):
        """ Draw on surface """
        # blit yourself at your current position
        surface.blit(self.image, (self.x, self.y))

class Rubbish(object): #represents all rubbish falling from top of gameDisplay
    def __init__(self):
        self.image = pygame.image.load(img_path1)
        self.x = random.randrange(0,display_width)
        self.y = -50
        dist = 10
        self.y = self.y + dist
        if self.y > display_height:
            self.x = random.randrange(0,display_width)
            self.y = -25       
    def draw(self, surface):
        """ Draw on surface """
        # blit yourself at your current position
        surface.blit(self.image, (self.x, self.y))

# ScoreFunction
def scorecounter(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Score:" + str(count), True, white)
    gameDisplay.blit(text, (0, 0))        
        
             
            
def mainRoutine(): 
    trash = Trash() # create an instance
    rubbish = Rubbish()
    background_image = pygame.image.load("background.png").convert() #where background image is loaded from. Background image must be in same folder as code
    score = 0
    running = True
    while running:
        # handle every event since the last frame.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() # quit the gameDisplay
                running = False
        scorecounter(score)
        trash.handle_keys() # handle the keys
        gameDisplay.blit(background_image, [0, 0]) #draws the background image to the gameDisplay before drawing the sprites
        trash.draw(gameDisplay) # draw the trashcan to the gameDisplay
        rubbish.draw(gameDisplay) #draw the rubbish to the gameDisplay  
        pygame.display.update() # update the gameDisplay with the trashcan, and rubbish sprites drawn onto it, instead of a black gameDisplay.        


    clock.tick(60)
mainRoutine()