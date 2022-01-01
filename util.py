import pygame
from pygame.locals import *
from sys import exit
import random
from termcolor import colored

# Height and Width
HEIGHT = 720
WIDTH = 1024

# RGB Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# The scores
LEFT_SCORE = 0
RIGHT_SCORE = 0

# The sounds
pygame.mixer.init()
paddleSound = pygame.mixer.Sound("assets/audio/paddel.wav")
scoreSound = pygame.mixer.Sound("assets/audio/score.wav")
wallSound = pygame.mixer.Sound("assets/audio/wall.wav")

# Wrap the given value according to arguments
def constrain(val, min_val, max_val):
    return min(max_val, max(min_val, val))
