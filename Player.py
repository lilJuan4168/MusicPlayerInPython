from pygame import mixer, mixer_music, event
from os import system, listdir
from classes import menu_music
from time import sleep

print("\n###---Chester's Music Player---###\n")
file = input("Pegar Direccion de Directorio:")
sleep(1)
system("clear")
canciones = listdir(file)
loop = True
menu = menu_music(canciones)
menu.new_list()

mixer.init()
while loop:
    print("\n###---Chester's Music Player---###\n")
    menu.show_list()  
    var = menu.choose()   
    if var == "play":
        mixer.music.load(file+"/"+menu.music[menu.count])  
        mixer.music.play()
    elif var == "pause":
        mixer.music.pause()
    elif var == "stop":
        mixer.music.stop()
    elif var == "unpause":
        mixer.music.unpause()
    elif var == "exit":
        loop = False
    system("clear")
mixer.quit()


    

