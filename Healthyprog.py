from pygame import mixer
from datetime import datetime
from time import time
def musicon(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a=input()
        if a== stopper:
            mixer.music.stop()
            break
def log_msg(msg):
    with open("mylogs.txt","a") as f:
        f.write(f"{msg} {datetime.now()}\n")
if __name__=='__main__':
    # musicon("water.mp3.ogg","stop")
    init_water = time()
    init_eyes = time()
    init_exer = time()
    watersec=40*60
    eyesec=30*60
    exersec=45*60
    while True:
        if time()-init_water > watersec:
            print("Please drink some water\nEnter 'drank' to stop the player")
            musicon("water.mp3.ogg",'drank')
            init_water=time()
            log_msg=("Drank water at")

        if time()-init_eyes > eyesec:
            print("Please do some eye exercise\nEnter 'eydone' to stop the player")
            musicon("water.mp3.ogg",'eydone')
            init_eyes=time()
            log_msg=("Done eyes excercise at")

        if time()-init_exer > exersec:
            print("Please do some physical activity\nEnter 'exdone' to stop the player")
            musicon("water.mp3.ogg",'exdone')
            init_exer=time()
            log_msg=("Done physical activity at")