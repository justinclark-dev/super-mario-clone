#!/usr/bin/python
import pygame
from classes import colors 
from pygame import mixer

# color variable to use the Color class
color = colors.Color

pygame.init()
mixer.init()

# create the screen (window) and set caption
screen = pygame.display.set_mode([1600,800])
screen.fill(color.skyblue)
pygame.display.set_caption('Super Mario Clone')

# mario theme music
themeSong = mixer.music.load('sound-files/mario-medley.mp3')
mixer.music.play()

# mario sounds
jumpSound = mixer.Sound('sound-files/smb_jump-small.wav')
stageClearSound = mixer.Sound('sound-files/smb_stage_clear.wav')
pipeSound = mixer.Sound('sound-files/smb_pipe.wav')
breakBrickSound = mixer.Sound('sound-files/smb_breakblock.wav')
coinSound = mixer.Sound('sound-files/smb_coin.wav')

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

coinSprites = pygame.sprite.Group()

coins = [Coin(500,105),Coin(700,105),Coin(1250,205),Coin(600,505),Coin(900,505)]

for coin in coins:
    coinSprites.add(coin)

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
        
    # create the ground
    pygame.draw.rect(screen,color.grassgreen,(0,700,1600,20)) # grass
    pygame.draw.rect(screen,color.dirtbrown,(0,720,1600,80)) # dirt
    
    # add a pipe
    pygame.draw.rect(screen,color.black,(1175,455,210,65)) # pipe upper
    pygame.draw.rect(screen,color.green,(1180,460,200,60))
    pygame.draw.rect(screen,color.black,(1195,455,170,265)) # pipe lower
    pygame.draw.rect(screen,color.green,(1200,460,160,260)) 

    # add bricks
    pygame.draw.rect(screen,color.black,(305,300,600,80)) # bricks
    pygame.draw.rect(screen,color.red,(300,305,600,80))

    coinSprites.update(x,y) 
    coinSprites.draw(screen)

    # mario height is roughly 210, ground starts at 700.
    if x > 1180 and x < 1210:
        if y > 250 and y < 280:
            pipeSound.play()

    if x > 300 and x < 900:
        if y > 300 and y < 380:
            breakBrickSound.play()            

    # =========================================================================
    ## set mario boundaries: 

    # left boundary
    if x == -1: 
        x = 0

    # top boundary
    if y < -210: y = -210

    # ground boundary (replace with boundary of object Mario is standing on)
    if y > 490: y = 490

    # right boundary
    if x == 1600:
        mixer.music.stop()
        stageClearSound.play()
    
    # pass end and through to begin again
    if x > 1800: 
        x = -200
        stageClearSound.stop()
        for coin in coins:
            coinSprites.add(coin)
        mixer.music.play()
    
    pygame.display.update()

pygame.quit()