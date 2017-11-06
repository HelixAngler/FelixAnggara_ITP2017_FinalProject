#Using cx_Freeze module
import cx_Freeze
#Importing os module
import os
#Get the TCL and TK directories
os.environ['TCL_LIBRARY'] = r'C:\Users\DarkHelix\AppData\Local\Programs\Python\Python36\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\DarkHelix\AppData\Local\Programs\Python\Python36\tcl\tk8.6'
#Variable to select which file that you want to have Its executable file
executing=[cx_Freeze.Executable("interface.py")]
#Run cx_Freeze and create needed files to run apps
cx_Freeze.setup(
    #Name of installer
    name="Bomb Disarming",
    #Describe the included files and packages
    options={"build_exe":{"packages":["pygame"],
                          "include_files":["alarm1.wav","BG.py","bloop_x.wav","bombardo.bmp",
                                           "Button1.png","Button2.png","Button_generate.py",
                                           "buzzer_x.wav","Cable.bmp","cartoon001.wav","chewy1.wav",
                                           "coin2.wav","cymbals.wav","disconnect_x.wav","homescr.bmp",
                                           "mechanism.py","randomizer_audio.py","stats.py","Timer.py",
                                           "timer arrow.png","timer frame.png"]}},
    #Select the files that will have its executable file
    executables = executing,
    #Describe the version of program
    version='1.0.0'
)