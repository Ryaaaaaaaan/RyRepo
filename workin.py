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

class Trash(pygame.sprite.Sprite):  # represents the trashcan, not the game
    def __init__(self):
        self.image = pygame.image.load(img_path)
        # the trashcans's position
        self.x = 0 #initial x value of trash can
        self.y = 680 #initial y value of trash can
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect = pygame.Rect(self.x,self.y,self.width,self.height)
    def handle_keys(self):
        """ Handles Keys """
        key = pygame.key.get_pressed()
        dist = 1 # distance moved in 1 frame, try changing it to 5
        if key[pygame.K_RIGHT] and self.rect.x < 950 - display_width-dist: # right key and no leaving the right hand side of the display
            self.rect.x += dist # move right
        elif key[pygame.K_LEFT] and self.rect.x>dist: # left key and no leaving the left side of the display. 
            self.rect.x -= dist #move left
    def draw(self, surface):
        """ Draw on surface """
        # blit yourself at your current position
        surface.blit(self.image,(self.rect.x, self.rect.y))

class Rubbish(pygame.sprite.Sprite): #represents all rubbish falling from top of gameDisplay
    def __init__(self):
        self.image = pygame.image.load(img_path1) #set the trash image to represent this sprite
        self.x = random.randrange(20,480) #spawn at random position on x axis
        self.y = -50 #initial y position of trash
        self.dist = 1 #speed of trash (in frames)
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect = pygame.Rect(self.x,self.y,self.width,self.height)        
    def draw(self, surface):
        """ Draw on surface """
        # blit yourself at your current position
        surface.blit(self.image,(self.rect.x, self.rect.y))

# ScoreFunction
def scorecounter(score):
    font = pygame.font.Font(None, 25) #font size 25
    text = font.render("Score:" + str(score), 1, white) #colour of text along with the prefix telling the user what the text represents, in this case it is 'score'
    gameDisplay.blit(text, (400, 650))  #draw text to the screen at 0,0      
        
             
            
def mainRoutine(): 
    trash = Trash() # create an instance for trash can
    score = 0 #initial value of the score
    rubbish = Rubbish() #create instance for trash
    background_image = pygame.image.load("background.png").convert() #where background image is loaded from. Background image must be in same folder as code
    running = True
    while running:
        # handle every event since the last frame.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() # quit the gameDisplay
                running = False
        trash.handle_keys() # handle the keys
        scorecounter(score) #calls the scorecounter function which is intended to make a score label appear showing the score variable value. 
        gameDisplay.blit(background_image, [0, 0]) #draws the background image to the gameDisplay before drawing the sprites
        trash.draw(gameDisplay) # draw the trashcan to the gameDisplay
        rubbish.draw(gameDisplay) #draw the rubbish to the gameDisplay
        """
        Collisions. States that when both object's assigned rectangles touch each other, the bottle will disappear and respawn at the top of the display, and the score will go up by one. When the score is 10, the game will end.
        """
        if pygame.sprite.collide_mask(rubbish,trash):
            rubbish.rect.x = random.randrange(20,480)
            rubbish.rect.y = display_height
            score = score +1
            print("Score:",score)
        if score == 10:
            pygame.quit()
            running = False
        """
        This is how I made the bottle fall from the top of the screen, and respawn on a random place on the 'x' axis, within the value of 20, and 480. It is not quite equal to the display width and height, but is close. I don't want the bottle to spawn on the borders, as then the whole sprite will not appear in frame and the player may not see the bottle, and in turn lose a life in an unjust manner.
        """
        rubbish.rect.y = rubbish.rect.y + rubbish.dist #attempt to make the sprite 'fall' 
        if rubbish.rect.y > display_height:
            rubbish.rect.x = random.randrange(20,480)
            rubbish.rect.y = -25
        pygame.display.update() # update the gameDisplay with the trashcan, and rubbish sprites drawn onto it, instead of a black gameDisplay.        


    clock.tick(60)
mainRoutine()