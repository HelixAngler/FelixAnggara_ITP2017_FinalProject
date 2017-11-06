#Importing Pygame
import pygame
#InGame Background Class
class Bggame:
    #Describe the background
    def __init__(self,screen_box):
        #Import the screen rectangle
        self.screen_box=screen_box
        #Load the image
        self.__background1 = pygame.image.load('bombardo.bmp')
        #Get the background rectangle
        self.__background1rect = self.__background1.get_rect()
        #Set the center of the background
        self.__background1rect.center = self.screen_box.center
    #Method to apply background to screen
    def blitbg(self,screen):
        #Print background to screen
        screen.blit(self.__background1,self.__background1rect)
#Menu background class
class Bghome:
    #Describe the background
    def __init__(self,screen_box):
        #Import the screen rectangle
        self.screen_box=screen_box
        #Load the image
        self.__background2 = pygame.image.load('homescr.bmp')
        #Get the background rectangle
        self.__background2rect = self.__background2.get_rect()
        #Set the center of the background
        self.__background2rect.center = self.screen_box.center
    #Method to apply background to screen
    def blitbg(self,screen):
        #Print background to screen
        screen.blit(self.__background2,self.__background2rect)