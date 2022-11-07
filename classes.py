from time import sleep
class menu_music:
    def __init__(self,list):
        self.music = sorted(list)
        self.music2 = []
        self.count = 0

    def new_list(self):
        for song in self.music:
            self.music2.append("🎵--> " + song)

    def show_list(self):
        for song in self.music:
            if self.music.index(song) == self.count:
                print(self.music2[self.count].upper())
                continue
            print(str(self.music.index(song))+ ". " + song.lower())

    def choose(self):
        user_in = input("Presione 'o' para subir,'l' para bajar y comandos 'play','pause','unpause','stop','exit'\n") 
        if (user_in == "l" or user_in == "L") and self.count < (len(self.music) -1):
            self.count += 1
        elif (user_in == "o" or user_in == "O") and self.count > 0:
            self.count -= 1
        elif user_in == "play" or user_in =="pause" or user_in=="stop" or user_in=="unpause" or user_in == "exit":
            return user_in
        else:
            print("Fuera del rango/comando indefinido")
            sleep(2)
            return "x"
        
        
