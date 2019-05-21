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
clock = pygame.time.Clock() #the game must run off a perception of time
gameDisplay = pygame.display.set_mode((display_width, display_height)) #sets size of gameDisplay/window in pixels
"""
The trash class includes everything related to the trashcan sprite, and defines how the trash can is controlled, the image that represents the trash can, where it spawns on the screen, and draws the rectangle that allows collisions. It also tells the game how to draw the trashcan to the screen.
"""
class Trash(pygame.sprite.Sprite):  # represents the trashcan, not the game
    def __init__(self):
        self.image = pygame.image.load(img_path)
        # the trashcans's position
        self.x = 0 #initial x value of trash can
        self.y = 650 #initial y value of trash can
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
"""
The rubbish class includes everything related to the rubbish sprite, and defines how the rubbish starts on the screen, the image that represents the rubbish, where it spawns on the screen, and draws the rectangle that allows collisions. It also tells the game to draw the rubbish to the screen.
"""
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
                    
"""
The main routine is basically everything that happens on the screen. Whence called, it draws everything to the screen, handles collisions, makes it possible to control the trashcan, and makes the rubbish fall from the screen.
"""
def mainRoutine(): 
    trash = Trash() # create an instance for trash can
    rubbish = Rubbish() #create instance for trash
    score = 0 #initial value of the score
    lives = 5
    font = pygame.font.Font(None, 25) #font size 25
    text = font.render("Score:" + str(score), 1, white) #colour of text along with the prefix telling the user what the text represents, in this case it is 'score'
    gameDisplay.blit(text, (400, 650))  #draw text to the screen at 0,0      
    background_image = pygame.image.load("background.png").convert() #where background image is loaded from. Background image must be in same folder as code
    running = True
    while running:
        # handle every event since the last frame.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() # quit the gameDisplay
                running = False
        trash.handle_keys() # handle the keys
        gameDisplay.blit(background_image, [0, 0]) #draws the background image to the gameDisplay before drawing the sprites
        trash.draw(gameDisplay) # draw the trashcan to the gameDisplay
        rubbish.draw(gameDisplay) #draw the rubbish to the gameDisplay
        """
        Collisions. States that when both object's assigned rectangles touch each other, the bottle will disappear and respawn at the top of the display, and the score will go up by one. When the score is 10, the game will end, and you will win. The lives variable starts at 5, and goes down one when you miss a piece of rubbish. When the lives variable hits 0, you lose the game. 
        """
        if pygame.sprite.collide_mask(rubbish,trash):
            rubbish.rect.x = random.randrange(20,480)
            rubbish.rect.y = -25
            score = score +1
            print("Score:",score)
        if score == 10:
            print ("******YOU WIN******")
            pygame.quit()
            running = False
        if rubbish.rect.y > 730 and not pygame.sprite.collide_mask(rubbish,trash): 
            lives = lives - 1
            rubbish.rect.x = random.randrange(20,480)
            rubbish.rect.y = -25            
            print("Lives:",lives)
        if lives == 0:
            print("******YOU LOSE******")
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


    clock.tick(30)
mainRoutine()

