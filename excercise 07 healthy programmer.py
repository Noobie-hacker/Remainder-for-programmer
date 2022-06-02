# Healthy Programmer Remainder
from datetime import datetime
from pygame import mixer
from time import time

def musiconloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        input_of_user=input()
        if input_of_user == stopper:
            mixer.music.stop()
            break
def log_now(msg):
    with open("mylogs.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n")
if __name__ == '__main__':
    init_water=time()
    init_eyes=time()
    init_excercise=time()
    watermins= 30*60
    exmins=50*60
    eyemins=40*60
while True:
    if time()-init_water>watermins:
        print("Water drinking time. Enter 'drank' to stop the alarm.")
        musiconloop("water.mp3",'drank')
        init_water=time()
        log_now("Drank water at ")

    if time()-init_eyes>eyemins:
        print("Eye massage time. Enter 'doneeye' to stop the alarm.")
        musiconloop("eyes.mp3",'doneeye')
        init_eyes=time()
        log_now("Eye massaged at ")

    if time()-init_excercise>exmins:
        print("Physical excercise time. Enter 'donephy' to stop the alarm.")
        musiconloop("physical.mp3",'donephy')
        init_excercise=time()
        log_now("Done excercise at ")
