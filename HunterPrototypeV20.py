import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(21, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)

from PIL import Image
from picamera import PiCamera
from time import sleep
import os
import numpy as np
from numpy import asarray

camera = PiCamera()

TotalPokemon = int(18)

PossiblePokemon = np.arange(0, TotalPokemon)
#print (PossiblePokemon)

PokemonValues = [225, 115, 58, 33, 214, 25, 173, 225, 0, 132, 197, 41, 156, 156, 173, 148, 140, 206, 255, 222, 0, 247, 206, 99, 214, 90, 140, 230, 132, 222, 255, 132, 74, 181, 25, 99, 74, 156, 189, 148, 214, 148, 90, 66, 41, 206, 90, 214, 165, 115, 82, 165, 123, 181]

notice = 0

while True:
 if notice == 0:
  print ('==========')

  print ('move left')
  GPIO.output(4, False)
  time.sleep(0.25)
  GPIO.output(4, True)
  time.sleep(0.5)
  GPIO.output(4, False)


  #Add Servo Movement left 1 block exactly (Make sure no buttons are being pressed afterwards)



  sleep(2)
  camera.start_preview()
  camera.capture('/home/pi/Desktop/Shiny_Hunter/Photos/picture%s.jpg' % i)
  camera.stop_preview()

  os.chdir('/home/pi/Desktop/Shiny_Hunter/Photos/')

  image = Image.open('picture%s.jpg' % i)

  data_A= asarray(image)

  sum = np.sum(data_A)

  print (sum)

  if sum > 80000000 :  #if the screen is white from the start of a battle
   print ('Battle')

   sleep(1) #Wait for white screen complete fade
   camera.start_preview() #the camera gets ready to take a photo of the battle and check for shiny sparkles
   camera.capture('/home/pi/Desktop/Shiny_Hunter/Battle_Photos/picture%s.jpg' % i) #A photo is taken
   camera.stop_preview() #the camera turns off

   os.chdir('/home/pi/Desktop/Shiny_Hunter/Battle_Photos/') #the directory changes so the code will access the battle photos

   img = Image.open('picture%s.jpg' % i) #turns the photo into a list of rgb values for each pixel
   WIDTH, HEIGHT = img.size

   data = list(img.getdata())

   data =[data[offset:offset+WIDTH] for offset in range(0, WIDTH*HEIGHT, WIDTH)]


   #notice = 0       #setting the shiny encounter on/off switch to zero as a reset because this is a new battle

   for row in data: #this code accesses the 3 int list for each pixel
    for i in row:
     Red = i[0]   #turns the 3 int into variables
     Green = i[1]
     Blue = i[2]

     if notice == 0:     #if a shiny hasn't been encountered
      for i in PossiblePokemon:
       if (PokemonValues[i*3]-1) <= Red <= (PokemonValues[i*3]+1):   #checking rgb values for something in shiny sparkle range
        #print("red")
        if (PokemonValues[(i*3)+1]-1) <= Green <= (PokemonValues[(i*3)+1]+1):
        # print("Green")
         if (PokemonValues[(i*3)+2]-1) <= Blue <= (PokemonValues[(i*3)+2]+1):
          print("Blue")
          notice = 1 #This prevents exiting the battle

   if notice == 0:   #if there was no shiny sparkle

    time.sleep(10)
    #use servo movements to exit battle

    GPIO.output(4, False)
    time.sleep(.25)
    GPIO.output(4, True)
    time.sleep(0.25)
    GPIO.output(4, False)

    time.sleep(1)

    GPIO.output(4, True)
    time.sleep(0.25)
    GPIO.output(4, False)

    time.sleep(1)

    GPIO.output(21, False)
    time.sleep(.25)
    GPIO.output(21, True)
    time.sleep(0.25)
    GPIO.output(21, False)

    time.sleep(1)

    GPIO.output(8, False)
    time.sleep(.25)
    GPIO.output(8, True)
    time.sleep(.25)
    GPIO.output(8, False)

 if notice == 0:
  #Servo Movement One Block Right (Make sure there is no buttons being pressed afterwards)
  print ('moving right')
  GPIO.output(21, False)
  time.sleep(.25)
  GPIO.output(21, True)
  time.sleep(0.25)
  GPIO.output(21, False)




  sleep(2)
  camera.start_preview()
  camera.capture('/home/pi/Desktop/Shiny_Hunter/Photos/picture%s.jpg' % i)
  camera.stop_preview()

  os.chdir('/home/pi/Desktop/Shiny_Hunter/Photos/')

  image = Image.open('picture%s.jpg' % i)

  data_A= asarray(image)

  sum = np.sum(data_A)

  print (sum)

  if sum > 80000000:  #if the screen is white from the start of a battle

   print ("battle")

   camera.start_preview() #the camera gets ready to take a photo of the battle and check for shiny sparkles
   sleep(3)               #the camera waits until the time shiny sparkles would appear
   camera.capture('/home/pi/Desktop/Shiny_Hunter/Battle_Photos/picture%s.jpg' % i) #A photo is taken
   camera.stop_preview() #the camera turns off

   os.chdir('/home/pi/Desktop/Shiny_Hunter/Battle_Photos/') #the directory changes so the code will access the battle photos

   img = Image.open('picture%s.jpg' % i) #turns the photo into a list of rgb values for each pixel
   WIDTH, HEIGHT = img.size

   data = list(img.getdata())

   data =[data[offset:offset+WIDTH] for offset in range(0, WIDTH*HEIGHT, WIDTH)]


   notice = 0       #setting the shiny encounter on/off switch to zero as a reset because this is a new battle

   for row in data: #this code accesses the 3 int list for each pixel
    for i in row:
     Red = i[0]   #turns the 3 int into variables
     Green = i[1]
     Blue = i[2]

     if notice == 0:     #if a shiny hasn't been encountered
      for i in PossiblePokemon:
       if (PokemonValues[(i*3)]-1) <= Red <= (PokemonValues[i*3]+1):   #checking rgb values for something in shiny sparkle range
        #print("red")
        if (PokemonValues[(i*3)+1]-1) <= Green <= (PokemonValues[(i*3)+1]+1):
         #print("Green")
         if (PokemonValues[(i*3)+2]-1) <= Blue <= (PokemonValues[(i*3)+2]+1):
          print("Blue")
          notice = 1 #This prevents exiting the battle

   if notice == 0:   #if there was no shiny sparkle

    time.sleep(10)

    #use servo movements to exit battle
    GPIO.output(4, False)
    time.sleep(.25)
    GPIO.output(4, True)
    time.sleep(0.25)
    GPIO.output(4, False)

    time.sleep(1)

    GPIO.output(4, True)
    time.sleep(0.25)
    GPIO.output(4, False)

    time.sleep(1)

    GPIO.output(21, False)
    time.sleep(.25)
    GPIO.output(21, True)
    time.sleep(0.25)
    GPIO.output(21, False)

    time.sleep(1)

    GPIO.output(8, False)
    time.sleep(.25)
    GPIO.output(8, True)
    time.sleep(.25)
    GPIO.output(8, False)
