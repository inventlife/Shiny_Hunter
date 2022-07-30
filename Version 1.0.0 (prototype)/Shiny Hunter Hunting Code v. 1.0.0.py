import time
import RPi.GPIO as GPIO
from RGBValues import PokemonValues

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(5, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

from PIL import Image
from picamera import PiCamera
from time import sleep
import os
import numpy as np
from numpy import asarray
from sys import exit

camera = PiCamera()

PossiblePokemon = np.arange(0, int((len(PokemonValues))/3)  )

Sensitivity = 1

def MoveA():
    GPIO.output(5, True)
    time.sleep(0.75)
    GPIO.output(5, False)

def MoveRight():
    GPIO.output(12, True)
    time.sleep(0.75)
    GPIO.output(12, False)

def MoveLeft():
    GPIO.output(21, True)
    time.sleep(0.75)
    GPIO.output(21, False)

def TakePhoto():
    camera.start_preview()
    camera.capture('/home/pi/Desktop/Shiny_Hunter/Photos/pictures.jpg')
    print("Photo Taken")    
    camera.stop_preview()

def TurnPhotoIntoSum():
    global sum 
    sum = int(0)
    os.chdir('/home/pi/Desktop/Shiny_Hunter/Photos/')
    image = Image.open('pictures.jpg')
    data_A= asarray(image)
    sum = np.sum(data_A)
    print(sum)

def ScanPhotoForColors():
    notice = 0
    img = Image.open('pictures.jpg')    #Convert photo into pixels
    WIDTH, HEIGHT = img.size
    data = list(img.getdata())
    data =[data[offset:offset+WIDTH] for offset in range(0, WIDTH*HEIGHT, WIDTH)]

    for row in data:
     for i in row:
      print (i)
      Red = i[0]
      Green = i[1]
      Blue = i[2]
      if notice == 0: #Continue if a shiny color wasn't detected in the previous pixel
       for i in PossiblePokemon:
           if (PokemonValues[i*3]-Sensitivity) <= Red <= (PokemonValues[i*3]+Sensitivity):   #checking rgb values for something in shiny sparkle range
            if (PokemonValues[(i*3)+1]-Sensitivity) <= Green <= (PokemonValues[(i*3)+1]+Sensitivity):
             if (PokemonValues[(i*3)+2]-Sensitivity) <= Blue <= (PokemonValues[(i*3)+2]+Sensitivity):
              print ("Shiny!")
              exit()
              notice = 1 #This prevents exiting the battle
#####################################################
#####################################################
notice = 0

while notice == 0:
    MoveLeft()
    time.sleep(2)
    TakePhoto()
    TurnPhotoIntoSum()

    if sum >= 75000000: #Battle has begun 
     notice = 0 
     print ("Battle has started")
     time.sleep(10) #Wait for transition and particles to ended
     TakePhoto()
     ScanPhotoForColors()

     time.sleep(2)
     TakePhoto()
     ScanPhotoForColors()

     if notice == 0: #If no shinies were encountered, leave the battle
      MoveLeft()
      time.sleep(0.75)
      MoveLeft()
      time.sleep(0.75)
      MoveRight()
      time.sleep(0.75)
      MoveA()
      time.sleep(10)

    MoveRight()
    time.sleep(2)
    TakePhoto()
    TurnPhotoIntoSum()

    if sum > 75000000: #Battle has begun
     notice = 0
     print ("Battle has started")
     time.sleep(12) #Wait for transition and particles to ended
     TakePhoto()
     ScanPhotoForColors()

     time.sleep(2)
     TakePhoto()
     ScanPhotoForColors()

     if notice == 0: #If no shinies were encountered, leave the battle
      MoveLeft()
      time.sleep(0.75)
      MoveLeft()
      time.sleep(0.75)
      MoveRight()
      time.sleep(0.75)
      MoveA()
      time.sleep(10)
