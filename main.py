#!/usr/bin/python
import pygame
from classes import colors 
import winsound
import pygame.mixer

pygame.init()

# create the screen (window) and set caption

screen = pygame.display.set_mode([1600,800])
pygame.display.set_caption('Super Mario Clone')

from pygame import mixer # Load the required library

# mario theme music
mixer.init()
themeSong = mixer.music.load('sound-files/mario-medley.mp3')

# mario sounds
jumpSound = pygame.mixer.Sound('sound-files/smb_jump-small.wav')
stageClearSound = pygame.mixer.Sound('sound-files/smb_stage_clear.wav')
pipeSound = pygame.mixer.Sound('sound-files/smb_pipe.wav')
breakBrickSound = pygame.mixer.Sound('sound-files/smb_breakblock.wav')
coinSound = pygame.mixer.Sound('sound-files/smb_coin.wav')

# color variable to use the Color class
color = colors.Color

# fill the background
screen.fill(color.skyblue)

# mario's starting point
marioImage = pygame.image.load('images/mario_sm.png')
x = -200 # we want to start him slightly off screen to the left
y = 490

class Coin(pygame.sprite.Sprite):
    WIDTH = 40
    HEIGHT = 80 
    def __init__(self, xCoord, yCoord):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((Coin.WIDTH, Coin.HEIGHT))
        self.image.fill(color.yellow)
        self.rect = self.image.get_rect()
        self.xCoord = xCoord
        self.yCoord = yCoord
        self.rect.topleft = (xCoord,yCoord)

    def update(self, xCoordMario, yCoordMario):
        if xCoordMario > self.xCoord - 100 and xCoordMario < self.xCoord:
            if yCoordMario > self.yCoord-80 and yCoordMario < self.yCoord + 80:
                coinSound.play()
                self.kill()

all_sprites = pygame.sprite.Group()
coin1 = Coin(500, 105)
coin2 = Coin(700, 105)
coin3 = Coin(1250, 205)
coin4 = Coin(600, 505)
coin5 = Coin(900, 505)

all_sprites.add(coin1, coin2, coin3, coin4, coin5)

# run game loop
done = False
while not done:

    # detect closing of window, then exit loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE: # mario jump
            jumpSound.play()
            screen.fill(color.skyblue)
            screen.blit(marioImage,(x,y))
            x = x + 2
            y = y - 6
        elif event.key == pygame.K_LEFT: # mario backward
            screen.fill(color.skyblue)
            screen.blit(pygame.transform.flip(marioImage, True, False),(x,y))
            x = x - 1
            y = y
        elif event.key == pygame.K_RIGHT: # mario forward
            screen.fill(color.skyblue)
            screen.blit(marioImage,(x,y))
            x = x + 1
            y = y
        elif event.key == pygame.K_UP: # mario down
            screen.fill(color.skyblue)
            screen.blit(marioImage,(x,y))
            x = x
            y = y - 1
        elif event.key == pygame.K_DOWN: # mario up
            screen.fill(color.skyblue)
            screen.blit(marioImage,(x,y))
            x = x
            y = y + 1
        
    # rect(where,color,(size)) size = (fromLeft, fromTop, width, length)

    # create the ground
    pygame.draw.rect(screen,color.grassgreen,(0,700,1600,20)) # grass
    pygame.draw.rect(screen,color.dirtbrown,(0,720,1600,80)) # dirt
    
    # add a pipe
    pygame.draw.rect(screen,color.black,(1175,455,210,65)) # pipe upper
    pygame.draw.rect(screen,color.green,(1180,460,200,60))
    pygame.draw.rect(screen,color.black,(1195,455,170,265)) # pipe lower
    pygame.draw.rect(screen,color.green,(1200,460,160,260)) 

    pygame.draw.rect(screen,color.black,(305,300,600,80)) # bricks
    pygame.draw.rect(screen,color.red,(300,305,600,80))

    all_sprites.update(x,y) 
    all_sprites.draw(screen)

    #mario height is roughly 210, ground is 700.
    if x > 1180 and x < 1210:
        if y > 250 and y < 280:
            pipeSound.play()

    if x > 300 and x < 900:
        if y > 300 and y < 380:
            breakBrickSound.play()            

    # set mario boundaries        
    if y > 490: y = 490
    if y < -200: y = -200
    if x == 1600:
        mixer.music.stop()
        stageClearSound.play()
    if x > 1800: 
        x = -200
        stageClearSound.stop()        
    if x < -200: x = 1800
    if x == -199: mixer.music.play()

    pygame.display.update()

pygame.quit()