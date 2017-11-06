#Importing modules
import time
import pygame
#Timer class
class Timing():
    #Initialize the timer
    def __init__(self,screen_box,screen):
        #Load the screen
        self.screen=screen
        #Get the screen rectangle
        self.screen_box=screen_box
        #Time limit setting
        self.timelimit=30
        #Reset the timer or get the timer components
        self.resettimes()
        #Initial Statement
        self.text="Disarm The Bomb"
    #Method to reset the timer or get the timer components
    def resettimes(self):
        #Set the counter time limit
        self.__counter=self.timelimit
        #Set initial number string for the counter (that will be shown on screen)
        self.text ='30'
        #Load timer arrow image
        self.timearrow = pygame.image.load('timer arrow.png')
        # Copy the timer arrow image
        self.timearrowcopy=self.timearrow
        #Load the timer frame image
        self.timeframe = pygame.image.load('timer frame.png')
        # Get timer arrow image rectangle
        self.timearrow_rect = self.timearrow.get_rect()
        #Set the time arrow coordinate
        self.timearrow_rect.centerx=self.screen_box.width-100
        self.timearrow_rect.centery=self.screen_box.centery-100
        #Get the copy of time arrow image rectangle
        self.timearrowcopy_rect=self.timearrow_rect
        #Get the timer frame image rectangle
        self.timeframe_rect = self.timeframe.get_rect()
        #Set the timer frame image coordinate
        self.timeframe_rect.centerx = self.screen_box.width - 100
        self.timeframe_rect.centery = self.screen_box.centery - 100
    #Method to decrease time
    def decrement(self,stat,buttons,numbering):
        #Check whether the counter is already zero or not
        if self.__counter > 0:
            #Reduce the counter value
            self.__counter -= 1
            #Change the number string to counter current value in the form of string
            self.text = str(self.__counter)
            #Move the timer arrow clockwise
            self.timearrowcopy=pygame.transform.rotate(self.timearrowcopy,(-360/self.timelimit))
            self.timearrowcopy_rect=self.timearrowcopy.get_rect(center=self.timearrow_rect.center)
        else:
            #Statement
            self.text = "GAME OVER!"
            #Stop the game
            stat.gamestart = False
            #Show the menu
            stat.showup = True
            #Empty the button list
            buttons.empty()
            #Reset the values of the lists
            numbering.ordered()
            numbering.numbers()
            numbering.audioassign()
    #Method to print the timer to screen
    def blittimer(self):
        #Print the timer frame to screen
        self.screen.blit(self.timeframe,self.timeframe_rect)
        #Print the timer arrow to screen
        self.screen.blit(self.timearrowcopy,self.timearrowcopy_rect)
