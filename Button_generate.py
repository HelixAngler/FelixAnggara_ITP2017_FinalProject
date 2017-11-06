#Import modules
import pygame
from pygame.sprite import Sprite
#Button class
class Button(Sprite):
    #Describe the button
    def __init__(self,screen,ident,looping):
        #Using inheritance to inherit Sprite
        super(Button,self).__init__()
        #Load the screen
        self.scrn=screen
        #Get the screen rectangle
        self.screen=self.scrn.get_rect()
        #Load the button image
        self.image=pygame.image.load('Cable.bmp')
        #Get image rectangle
        self.rect=self.image.get_rect()
        #Create the the first position coordinate minus 50 by dividing the height of the screen into eight
        self.coordfirst=(self.screen.height / 8)
        #Set thge multiplier number for coordinate position
        self.multiplier=50
        #Create the multiplier for the position
        self.multiplying=(self.multiplier*looping)
        #Generate the Y-coordinate
        self.Y_coordinate=self.coordfirst+self.multiplying
        #Set image coordinates
        self.rect.centery = self.Y_coordinate
        self.rect.centerx = self.screen.centerx
        #Set the button ID
        self.ident=ident
    #Method to create the button on screen
    def create(self):
        #Print the button
        self.scrn.blit(self.image,self.rect)
#Start button class
class Trigger:
    #Describe the button
    def __init__(self,screen):
        #Load the screen
        self.scrn=screen
        #Get the creen rectangle
        self.screen = self.scrn.get_rect()
        #Load the start button image
        self.image = pygame.image.load('Button1.png')
        #Get the image rectangle
        self.rect = self.image.get_rect()
        #Set the position of the button started from the center of screen
        self.coordY=-50
        #Set the button coordinates
        self.rect.centery = self.screen.centery+self.coordY
        self.rect.centerx = self.screen.centerx
    #Method to print the button
    def blitit(self):
        #Print the button to screen
        self.scrn.blit(self.image,self.rect)
#Exit button class
class Exiting:
    #Describe the button
    def __init__(self,screen):
        #Load the screen
        self.scrn=screen
        #Get the screen rectangle
        self.screen = self.scrn.get_rect()
        #Load the exit button image
        self.image = pygame.image.load('Button2.png')
        #Get the image rectangle
        self.rect = self.image.get_rect()
        #Set the position of the button started from the center of screen
        self.coordY=50
        #Set the button coordinates
        self.rect.centery = self.screen.centery+self.coordY
        self.rect.centerx = self.screen.centerx
    #Method to print the button
    def blitit(self):
        #Print the button to screen
        self.scrn.blit(self.image,self.rect)
