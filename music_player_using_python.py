from pygame import mixer
mixer.init()
mixer.music.load("E:/New folder (4)/Songs/Pehla Pyaar.mp3")
mixer.music.set_volume(1.0)
mixer.music.play(0)
while True:
    print("Press 'p' to pause, 'r' to resume")
    print("Press 'e'to exit")
    query=input(">>> ")
    if query=='p':
        mixer.music.pause()
    elif query=='r':
        mixer.music.unpause()
    elif query=='e':
        mixer.music.stop()
        break
