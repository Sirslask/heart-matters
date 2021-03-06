#! /usr/bin/python

#  soundobject.py
#
#  Copyright 2013 Harry Nystad <harryjnystad@gmail.com>
#
#  This game and all content in this file is licensed under the 
#  Attribution-Noncommercial-Share Alike 3.0 version of the Creative Commons License.
#  For reference the license is given below and can also be found at 
#  http://creativecommons.org/licenses/by-nc-sa/3.0/
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
#
#

import pygame
from image import *
from hmglobals import DEBUG

class SoundObject(pygame.sprite.Sprite):
	""" Object class for sound-objects.
	"""
	def __init__ (self, sound, pos):
		if DEBUG > 2:
			print("in Object.__init__()")
			print(soundPath)
		soundPath = "res/sound/"+sound
		pygame.sprite.Sprite.__init__(self)
		self.rect = pygame.Rect(10,10,10,10) # This is the default size of a sound object on the map
		self.sound = pygame.mixer.Sound(soundPath)
		screen = pygame.display.get_surface()
		self.scrArea = screen.get_rect()
		self.rect = self.rect.move(pos)
		self.playSound()
	#end __ init__

	def playSound(self, loop= (-1)):
		self.sound.play(loop)
	#play end

	def stopSound(self):
		self.sound.stop()
	#stop end

	def volumeControler(self,playerPos):
		difX = 0
		difY = 0
		volume= 0.0

		if playerPos[0] > self.rect[0]:
			difX =  playerPos[0] - self.rect[0]
		else:
			difX =  self.rect[0] - playerPos[0]

		if playerPos[1] > self.rect[1]:
			difY =  playerPos[1] - self.rect[1]
		else:
			difY =  self.rect[1] - playerPos[1]


		difX =  playerPos[0] - self.rect[0]
		difY =  playerPos[1] - self.rect[1]

		difpos = pygame.math.Vector2(difX,difY)


		if DEBUG > 2:
			print(difpos)

		if difpos[0] > 200 or difpos[1] > 200:
			self.sound.set_volume(0.0)
		if difpos[0] < 200 and difpos[1] < 200:
			self.sound.set_volume(0.2)
		if difpos[0] < 100 and difpos[1] < 100:
			self.sound.set_volume(0.5)
		if difpos[0] < 50 and difpos[1] < 50:
			self.sound.set_volume(1)
	#end volumControler
#end soundObject
