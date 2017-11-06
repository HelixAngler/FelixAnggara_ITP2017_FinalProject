#Import modules and custom classes
import pygame
from pygame.sprite import Group
import sys
from Button_generate import *
from randomizer_audio import *
import mechanism as me
from stats import Status
from Timer import *
from BG import*
#Creating function for running the game
def rungame():
    #Initiate pygame
    pygame.init()
    #Set the screen width
    width=1200
    #Set the screen height
    height=800
    #Set screen resolution
    screen=pygame.display.set_mode((width,height))
    #Get the reactangle area from screen (width, height, coordinates inside the screen box)
    screen_box=screen.get_rect()
    #Set the title to "Bomb Disarming"
    pygame.display.set_caption("Bomb Disarming")
    #Import the background classes
    bakgrogame=Bggame(screen_box)#Assigned to bakgrogame
    bakgrohome=Bghome(screen_box)#Assigned to bakgrohome
    #Scan the time tick in second (1000ms)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    #Generate font called 'font' and set 'font' style to Consolas with the size of 30
    font = pygame.font.SysFont('Consolas', 30)
    #Import timer class called 'Timing'
    ticking=Timing(screen_box,screen)
    #Import randomizer class called 'Randomizing'
    numbering=Randomizing()
    #Create sprite list for storing buttons
    buttons=Group()
    #Import 'Status' class
    stat=Status()
    #Import trigger game button class called 'Trigger'
    trig=Trigger(screen)
    #Import quit game button class called 'Exiting'
    quiting=Exiting(screen)
    #Start the loop
    while True:
        #fill the screen with white base background
        screen.fill((255, 255, 255))
        #Check the hardware event
        me.checkev(numbering,buttons,stat,trig,quiting,ticking)
        #Update button list
        buttons.update()
        #If the game is started
        if stat.gamestart:
            #Show ingame background called 'bakgrogame'
            bakgrogame.blitbg(screen)
            #Show the stopwatch-like timer
            ticking.blittimer()
            #Scan if button list empty
            if len(buttons) == 0:
                #Move mouse cursor to (0, 0)
                pygame.mouse.set_pos(0, 0)
                #Reset timer
                ticking.resettimes()
                #Generate 8 Buttons
                for a in range(1, 9):
                    #Generate button ID number
                    numberid = numbering.modify()
                    #Generate button
                    switch = Button(screen, numberid, a)
                    #Assign music to button with specific ID
                    numbering.soundassigning(switch.ident)
                    #Add button to the list
                    buttons.add(switch)
                #Play the sound started from the button with the ID of 1
                Music(numbering.assignsound[numbering.comparing[0]])
        #If the game isn't started or is already finished
        if stat.showup:
            #Show menu background called 'backgrohome'
            bakgrohome.blitbg(screen)
            #Show trigger game button
            trig.blitit()
            #Show quit game button
            quiting.blitit()
        #Show buttons from button list
        for btn in buttons:
            btn.create()
        #Show numberical timer, Game Over, and Congrats
        screen.blit(font.render(ticking.text, True, (255, 0, 0), (255, 255, 255)),(screen_box.centerx, screen_box.height - 100))
        #Update screen using flip
        pygame.display.flip()
#Run the function
rungame()
