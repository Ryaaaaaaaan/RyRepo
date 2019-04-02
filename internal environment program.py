import pygame
import os
import time
import random
from pygame.locals import *
pygame.init() #starts pygame
img_path = os.path.join('C:\Python34', 'trash.png') #where each sprite image is loaded from in the computer
img_path1 = os.path.join('C:\Python34', 'rubbish.png')
display_width = 500 #value of the width of the display (in pixels)
display_height = 750 #value of the height of the display (in pixels)
white = (255,255,255) #sets the value of variable 'white' instead of having to type the 255,255,255 everytime. 
clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode((display_width, display_height)) #sets size of gameDisplay/window in pixels

class Trash(object):  # represents the trashcan, not the game
    def __init__(self):
        self.image = pygame.image.load(img_path)
        # the trashcans's position
        self.x = 0 #initial x value of trash can
        self.y = 0 #initial y value of trash can
        self.Rect = self.image.get_rect()
    def handle_keys(self):
        """ Handles Keys """
        key = pygame.key.get_pressed()
        dist = 1 # distance moved in 1 frame, try changing it to 5
        if key[pygame.K_DOWN] and self.y < 1400 - display_height-dist: # down key and no leaving bottom of display
            self.y += dist # move down
        elif key[pygame.K_UP] and self.y>dist: # up key and no leaving the top of the display
            self.y -= dist # move up
        if key[pygame.K_RIGHT] and self.x < 950 - display_width-dist: # right key and no leaving the right hand side of the display
            self.x += dist # move right
        elif key[pygame.K_LEFT] and self.x>dist: # left key and no leaving the left side of the display. 
            self.x -= dist #move left
            
            
            

    def draw(self, surface):
        """ Draw on surface """
        # blit yourself at your current position
        surface.blit(self.image, self.Rect,(self.x, self.y))

class Rubbish(object): #represents all rubbish falling from top of gameDisplay
    def __init__(self):
        self.image = pygame.image.load(img_path1) #set the trash image to represent this sprite
        self.x = random.randrange(0,display_width) #spawn at random position on x axis
        self.y = -50 #initial y position of trash
        self.dist = 1 #speed of trash (in frames) 
        self.Rect = self.image.get_rect()
    def draw(self, surface):
        """ Draw on surface """
        # blit yourself at your current position
        surface.blit(self.image,self.Rect, (self.x, self.y))

# ScoreFunction
def scorecounter(count):
    font = pygame.font.SysFont(None, 25) #font size 25
    text = font.render("Score:" + str(count), True, white) #colour of text along with the prefix telling the user what the text represents, in this case it is 'score'
    gameDisplay.blit(text, (0, 0))  #draw text to the screen at 0,0      
        
             
            
def mainRoutine(): 
    trash = Trash() # create an instance for trash can
    rubbish = Rubbish() #create instance for trash
    background_image = pygame.image.load("background.png").convert() #where background image is loaded from. Background image must be in same folder as code
    score = 0 #initial value of the score
    running = True
    while running:
        # handle every event since the last frame.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() # quit the gameDisplay
                running = False
        trash_rect = trash.Rect(center=(trash.x,trash.y))
        rubbish_rect = rubbish.Rect(center=(rubbish.x,rubbish.y))
        if trash_rect.colliderect(rubbish_rect):
            rubbish.x = random.randrange(0,display_width)
            rubbish.y = -25
            score = score +1

        scorecounter(score)
        trash.handle_keys() # handle the keys
        gameDisplay.blit(background_image, [0, 0]) #draws the background image to the gameDisplay before drawing the sprites
        trash.draw(gameDisplay) # draw the trashcan to the gameDisplay
        rubbish.draw(gameDisplay) #draw the rubbish to the gameDisplay
        rubbish.y = rubbish.y + rubbish.dist #attempt to make the sprite 'fall' 
        if rubbish.y > display_height:
            rubbish.x = random.randrange(0,display_width)
            rubbish.y = -25         
        pygame.display.update() # update the gameDisplay with the trashcan, and rubbish sprites drawn onto it, instead of a black gameDisplay.        


    clock.tick(60)
mainRoutine()