# Healthy Programmer
print(f"Welcome to Healthy Programmer by Soumya\n")
import time
from pygame import mixer

def getdate():
    """

    :return: it returns date and time
    """
    import datetime
    return datetime.datetime.now()

date = str(getdate())


def IsOfficeTime(currenttime):
    """

    :param currenttime:
    :return:  True or False
    """
    if currenttime > '09:00:00' and currenttime < '17:00:01':
        return True
    else:
        return False


def eyes_music():
    """
    eyes music function
    :return:
    """
    # Starting the mixer
    mixer.init()

    # Loading the song
    mixer.music.load("eyes.mp3")

    # Setting the volume
    mixer.music.set_volume(0.7)

    # Start playing the song
    mixer.music.play()


def exe_music():
    """
    exercise music func
    :return:
    """

    # Starting the mixer
    mixer.init()

    # Loading the song
    mixer.music.load("Physical.mp3")

    # Setting the volume
    mixer.music.set_volume(0.7)

    # Start playing the song
    mixer.music.play()


def water_music():
    """
    water music func
    :return:
    """
    # Starting the mixer
    mixer.init()

    # Loading the song
    mixer.music.load("Water.mp3")

    # Setting the volume
    mixer.music.set_volume(0.7)

    # Start playing the song
    mixer.music.play()


NumberofWaterRemaining = 18
WaterAfterEvery = 1200                       # Seconds  - 20 minutes
EyeExerciseAfterEvery = 1800                  # Seconds - 30 minutes
PhysicalExerciseAfterEvery = 2700              # Seconds  - 45 minutes
water_msc = water_music()
eyes_msc = eyes_music()
physicsl_msc = exe_music()

currenttime = time.strftime('%H:%M:%S')
WaterTakenAt = time.time()
EyeExerciseAt = time.time()
PhysicalExerciseAt = time.time()

SleepTime = 60                                # Sleep time in seconds It will check after every 60 seconds.

while (IsOfficeTime(currenttime)):
            #     Check for water
     if NumberofWaterRemaining > 0:
        if (time.time() - WaterTakenAt) > WaterAfterEvery:     # water after every 20 minutes
            print("Time to drink water\n")
            while True:
                water_msc = water_music()
                if input("Enter Done if you had water: ").lower() == "done":
                    WaterTakenAt = time.time()
                    with open("water.txt", "a") as f:
                        f.write(date)
                    NumberofWaterRemaining -= 1
                    break
                if time.time() - EyeExerciseAt > EyeExerciseAfterEvery:
                    print("Time to do eye exercise\n")
                    while True:
                        eyes_msc = eyes_music()
                        if input("Enter Done if you done eye exercise : ").lower() == "done":
                            EyeExerciseAt = time.time()
                            with open("eyes_exe.txt", "a") as f:
                                f.write(date)
                            break
                if time.time() - PhysicalExerciseAt > PhysicalExerciseAfterEvery:
                    print("Time to do Physical exercise")
                    while True:
                        physicsl_msc = exe_music()
                        if input("Enter Done if you done Physical exercise : ").lower() == "done":
                            PhysicalExerciseAt = time.time()
                            with open("Physical_exe.txt", "a") as f:
                                f.write(date)
                            break

time.sleep(SleepTime)
currenttime = time.strftime('%H:%M:%S')
