from pygame import mixer
mixer.init() #starting the music
mixer.music.load("E:/New folder (4)/Songs/Pehla Pyaar.mp3") #loading music
mixer.music.set_volume(1.0) #setting volume in range 0.0 to 1.0
mixer.music.play(0) #0 for one play and -1 for infinite play
while True:
    print("Press 'p' to pause, 'r' to resume")
    print("Press 'e'to exit")
    query=input(">>> ")
    if query=='p':
        mixer.music.pause() #to pause music
    elif query=='r':
        mixer.music.unpause()#to resume music
    elif query=='e':
        mixer.music.stop() #to stop music
        break
