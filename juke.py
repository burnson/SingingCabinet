#!/usr/bin/python

print('...Importing libraries...')
import commands
import glob
import os
import pygame
import random
import time
import RPi.GPIO as GPIO

def shellquote(s):
  return "'" + s.replace("'", "'\\''") + "'"

print('...Initializing audio...')
pygame.mixer.init(44100)

print('...Initializing switch...')
GPIO.setmode(GPIO.BCM)

# Set open/close switch between ground and Pin 18
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

print('...Discovering audio files...')
files = glob.glob('/mnt/tunez/*.ogg')
print str(len(files)) + ' files found'

print('...Polling...')

prev_input = 0
while True:
  input = GPIO.input(18)
  if input:
    print('OPEN')
  else:
    print('CLOSED')
  if(prev_input and (not input)):
    print('...Door is CLOSED...')
    print('...Stopping audio playback...')
    if(pygame.mixer.music.get_busy()):
      pygame.mixer.music.fadeout(2000)
  if((not prev_input) and input):
    print('...Door is OPEN...')
    print('...Picking audio file...')
    pick = random.randint(0, len(files) - 1)
    file = files[pick]
    print('Picked file ' + str(pick) + ': ' + file)
    length = int(float(commands.getoutput('soxi -D ' + shellquote(file))))
    print('...Track is ' + str(length) + ' seconds...')
    pygame.mixer.music.load(file)
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play(-1, random.randint(0, length - 5))
  prev_input = input
  time.sleep(0.25)
