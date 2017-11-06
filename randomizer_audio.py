#Import modules
import pygame
import random
#Randomizer Class To assign ID and sound randomly
class Randomizing:
    #Initialize values from other methods
    def __init__(self):
        self.ordered()
        self.numbers()
        self.audioassign()
    #Method of comparison list to compare IDs and to reset comparison list
    def ordered(self):
        self.comparing = [1, 2, 3, 4, 5, 6, 7, 8]
    #Method of ID list consisted of IDs that will be assigned to Buttons and reset ID list
    def numbers(self):
        self.list=[1,2,3,4,5,6,7,8]
    #Method of assigning alphabet to the IDs (the alphabet represents sounds that will be played (music class for furter configuration)
    def audioassign(self):
        #Dictionary for storing the alphabets to the IDs
        self.assignsound={1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:''}
        #Alphabets list
        self.__alphabet=['a','b','c','d','e','f','g','h']
    #Method to modify the ID list and assigning the IDs
    def modify(self):
        #Choose the IDs randomly
        assigninglist=random.choice(self.list)
        #Remove the ID trace inside the list to prevent one ID to be assigned to more than one button
        self.list.remove(assigninglist)
        #Outputting the ID from the method to outside the class
        return assigninglist
    #Method for modify alphabet list and assigning the alphabets
    def soundassigning(self,idassign):
        #Choose the alphabet randomly
        self.assigning=random.choice(self.__alphabet)
        #Assign the alphabet to the specific ID dictionary
        self.assignsound[idassign]=self.assigning
        #Remove the alphabet to prevent one aphabet to be assigned to more than one button
        self.__alphabet.remove(self.assigning)
    #Method to delete the first number of comparison list to prevent scanning for the ID that no longer exist (if button with ID 1 has already been removed, it will scan for button with ID 2)
    def removing(self):
        #Delete command
        del self.comparing[0]
#Music class for identify the sound that must to be played
class Music:
    #Initialize 'Music' class
    def __init__(self,checker):
        #Check the alphabet inside the ID dictionary, and play the specific sounds
        #Load music, then play once
        #pygame.mixer.music.load("") to load  the sound
        #pygame.mixer.music.play(1) to play te sound without loop
        if checker=='a':
            pygame.mixer.music.load("chewy1.wav")
            pygame.mixer.music.play(1)
        elif checker=='b':
            pygame.mixer.music.load("alarm1.wav")
            pygame.mixer.music.play(1)
        elif checker=='c':
            pygame.mixer.music.load("bloop_x.wav")
            pygame.mixer.music.play(1)
        elif checker=='d':
            pygame.mixer.music.load("buzzer_x.wav")
            pygame.mixer.music.play(1)
        elif checker=='e':
            pygame.mixer.music.load("cartoon001.wav")
            pygame.mixer.music.play(1)
        elif checker=='f':
            pygame.mixer.music.load("coin2.wav")
            pygame.mixer.music.play(1)
        elif checker=='g':
            pygame.mixer.music.load("cymbals.wav")
            pygame.mixer.music.play(1)
        elif checker=='h':
            pygame.mixer.music.load("disconnect_x.wav")
            pygame.mixer.music.play(1)
