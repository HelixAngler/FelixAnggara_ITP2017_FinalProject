#Import modules
import pygame
import sys
import time
#Import custom class, music
from randomizer_audio import Music
#Checking event function
def checkev(numbering,buttons,stat,menustart,menuexit,ticking):
    #Check occured event
    for event in pygame.event.get():
        #Get cursor positions
        cursorx, cursory = pygame.mouse.get_pos()
        #If the event is quit, then It will close the program
        if event.type==pygame.QUIT:
            #Exit program
            sys.exit()
        #If mouseclick, then It will trigger checking the click positions
        if event.type==pygame.MOUSEBUTTONDOWN:
            #Check click position
            button_click(numbering,buttons,cursorx,cursory,stat,menustart,menuexit,ticking)
        #If cursor above the button, then, It will play sound based from the alphabet inside the ID dictionary
        if event.type==pygame.MOUSEMOTION:
            #Check on every buttons
            for clicking in buttons:
                #Check collide point
                if clicking.rect.collidepoint(cursorx, cursory):
                    #Get the alphabet from ID dictionary
                    soundclue=numbering.assignsound[clicking.ident]
                    #Play the sound
                    Music(soundclue)
        #This will be triggered by USEREVENT event
        if event.type == pygame.USEREVENT:
            #Activate when game is running
            if stat.gamestart:
                #Check if there are still buttons inside the list
                if len(buttons)>0:
                    #Decrease time using function
                    ticking.decrement(stat,buttons,numbering)
#Button click Function
def button_click(numbering,checking,cursorx,cursory,stat,menustart,menuexit,ticking):
    #Check when it's started
    if stat.gamestart:
        #Check whether the checking is empty or not (button list)
        if len(checking) != 0:
            #Check every button(clicking) in list(checking)
            for clicking in checking:
                #Check collision between cursor click and clicking
                if clicking.rect.collidepoint(cursorx, cursory):
                    #Check whether the ID of clicking is match with the comparing list or not
                    if clicking.ident == numbering.comparing[0]:
                        #Removing the comparing value that is match with clicking ID
                        numbering.removing()
                        #Remove clicking from checking
                        checking.remove(clicking)
                        #Update checking
                        checking.update()
                        #Check the comparing list whether is empty or not
                        if len(numbering.comparing) > 0:
                            #Play the next sound based from the ID
                            Music(numbering.assignsound[numbering.comparing[0]])
                        else:
                            #Statement
                            ticking.text="CONGRATULATION!"
                            #Stop the game
                            stat.gamestart = False
                            #Show the menu
                            stat.showup = True
                            #Emptying checking
                            checking.empty()
                            #Reset the values of the lists
                            numbering.ordered()
                            numbering.numbers()
                            numbering.audioassign()
                    else:
                        #Statement
                        ticking.text="GAME OVER!"
                        #Stop the game
                        stat.gamestart=False
                        #Show the menu
                        stat.showup=True
                        #Empty the list
                        checking.empty()
                        #Reset the values of the lists
                        numbering.ordered()
                        numbering.numbers()
                        numbering.audioassign()
    else:
        #Check whether the menu is triggered or not
        if stat.showup:
            #Check if the mouseclick is on the start button
            if menustart.rect.collidepoint(cursorx, cursory):
                #Start the game
                stat.gamestart=True
                #Hide the menu
                stat.showup=False
            #Check if the mouseclick in on the exit button
            if menuexit.rect.collidepoint(cursorx, cursory):
                #Close the program
                sys.exit()
