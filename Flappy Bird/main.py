import random
import sys
import pygame
from pygame.locals import *

# Global Variables for this game.

framesPerSecond = 32
screenheight = 511
screenWidth = 289
displayScreen = pygame.display.set_mode((screenWidth, screenheight))
groundY = screenheight * 0.8 # --> Base/Ground of the game.
gameSprites = {} # -->  Sprite Dictionary
gameSounds = {}  # -->  Sounds Dictionary
player = 'gallery/sprites/bird.png'
background = 'gallery/sprites/background.png'
pipe = 'gallery/sprites/pipe.png'

# Functions for this Game:

def welcomeScreen(): # --> This function shows welcome screen as long as no key is pressed.

    playerx = int(screenWidth/5)
    playery = int((screenheight - gameSprites['player'].get_height())/2)

    messagex = int((screenWidth - gameSprites['message'].get_width())/2)
    messagey = int(screenheight * 0.13)

    basex = 0

    while True:

        for event in pygame.event.get(): # --> pygame.event.get() tells about events input by user ie Mouse key pressed etc

            # If user clicks cross button then exit the game.
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            # If the user press sapce key or up key start the game.
            elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                return

            # screen.blit() takes image and (x,y) coordinates as arguments.
            else:
                
                displayScreen.blit(gameSprites['background'],(0,0))       
                displayScreen.blit(gameSprites['player'],(playerx,playery))       
                displayScreen.blit(gameSprites['message'],(messagex,messagey))       
                displayScreen.blit(gameSprites['base'],(basex,groundY))    

                pygame.display.update() # --> This function is necessary to blit the screen.
                FPS_Clock.tick(framesPerSecond) # --> To control Frame Rate.

def mainGame(): # This is the main Game Functions.

    score = 0
    playerx = int(screenWidth/5) 
    playery = int(screenWidth/2) 
    basex = 0

    # Create 2 Pipes on the screen.
    pipe1 = getRandomPipe()
    pipe2 = getRandomPipe()

    # Create List of Upper Pipe.
    upperPipes = [
        {'x': screenWidth+200 , 'y': pipe1[0]['y']},
        {'x': screenWidth+200+(screenWidth/2) , 'y': pipe2[0]['y']},
    ]

    # Create List of lower Pipe.
    lowerPipes = [
        {'x': screenWidth+200 , 'y': pipe1[1]['y']},
        {'x': screenWidth+200+(screenWidth/2) , 'y': pipe2[1]['y']},
    ]

    # Velocity of the Player(Bird) and Pipe.
    pipeVelocityX = -4
    playerVelocityY = -9
    playerMaxVelocityY = 10
    playerMinVelocityY = -8
    playerAccelerationY = 1
    
    playerFlapVecity = -8 # --> Velocity of the Player(Bird) while flappping.
    playerFlapped = False # --> Only True when the bird is Flapping.

    # Main Game Loop.
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN or (event.key == K_SPACE or event.key == K_UP):
                if playery > 0:
                    playerVelocityY = playerFlapVecity
                    playerFlapped = True
                    gameSounds['wing'].play()

        crashTest = isCollide(playerx, playery, upperPipes, lowerPipes) # --> This Function will return True if you are crashed. 

        if crashTest:
            return
    
        # Score Check.

        playerMidPos = playerx + gameSprites['player'].get_width()/2
        for pipe in upperPipes:
            pipeMidPos = pipe['x'] + gameSprites['pipe'][0].get_width()/2
            if pipeMidPos<= playerMidPos < pipeMidPos +4:
                score +=1
                print(f"Your score is {score}") 
                gameSounds['point'].play()


        if playerVelocityY < playerMaxVelocityY and not playerFlapped:
            playerVelocityY += playerAccelerationY

        if playerFlapped:
            playerFlapped = False

        playerHeight = gameSprites['player'].get_height()
        playery = playery + min(playerVelocityY, groundY - playery - playerHeight)

            # Move Pipes to the Left.
        for upperPipe, lowerPipe in zip(upperPipes,lowerPipes):
            upperPipe['x'] += pipeVelocityX
            lowerPipe['x'] += pipeVelocityX

            # Add a new pipe when the previous pipe is about to cross leftmost part of the screen.
        if 0<upperPipes[0]['x']<5:
            newPipe = getRandomPipe()
            upperPipes.append(newPipe[0])
            lowerPipes.append(newPipe[1])

            # If the pipe is out of the screen Remove it.
        if upperPipes[0]['x'] < - gameSprites['pipe'][0].get_width():
            upperPipes.pop(0)
            lowerPipes.pop(0)

            # Let's Start Blitting our Sprites now.

        displayScreen.blit(gameSprites['background'],(0,0))    
       
        for upperPipe, lowerPipe in zip(upperPipes,lowerPipes):
            displayScreen.blit(gameSprites['pipe'][0],(upperPipe['x'],upperPipe['y']))     
            displayScreen.blit(gameSprites['pipe'][1],(lowerPipe['x'],lowerPipe['y']))     

        displayScreen.blit(gameSprites['player'],(playerx,playery))  
        displayScreen.blit(gameSprites['base'],(basex,groundY))   

        myDigits = [int(x) for x in list(str(score))] 
        width = 0
        for digits in myDigits:
            width += gameSprites['numbers'][digits].get_width()

        xOffset = (screenWidth - width)/2
            
        for digits in myDigits:

            displayScreen.blit(gameSprites['numbers'][digits],(xOffset, screenheight*0.12))     
            xOffset += gameSprites['numbers'][digits].get_width()

        pygame.display.update() # --> This function is necessary to blit the screen.
        FPS_Clock.tick(framesPerSecond) # --> To control Frame Rate.

def isCollide(playerx, playery, upperPipes, lowerPipes):
    if playery> groundY - 25  or playery<0:
        gameSounds['hit'].play()
        return True

    for pipe in upperPipes:
        pipeHeight = gameSprites['pipe'][0].get_height()
        if(playery < pipeHeight + pipe['y'] and abs(playerx - pipe['x']) < gameSprites['pipe'][0].get_width()):
            gameSounds['hit'].play()
            return True

    for pipe in lowerPipes:
        if (playery + gameSprites['player'].get_height() > pipe['y']) and abs(playerx - pipe['x']) < gameSprites['pipe'][0].get_width():
            gameSounds['hit'].play()
            return True

    return False

def getRandomPipe(): # --> Generates location of the pipes to blit them on the screen.
    pipeHeight = gameSprites['pipe'][0].get_height()
    offset = screenheight/4.5
    
    y2 = offset + random.randrange(0,int(screenheight-gameSprites['base'].get_height() - 1.2*offset))
    
    pipex = screenWidth + 10

    y1 = pipeHeight - y2 + offset

    pipe = [
        {'x':pipex, 'y': -y1}, # Upper Pipe
        {'x':pipex, 'y': y2}  # Lower Pipe
    ]
 
    return pipe

    
if __name__ == "__main__": # -->  Point from where the logic of the game will start.

    pygame.init() # --> Initialize all Pygame Modules.

    FPS_Clock = pygame.time.Clock() # --> It is used to control frames per second (FPS) of the game.

    pygame.display.set_caption('Flappy Bird By Syed Hussain') 

    # Game Sprites:
    # convert_alpha optimizes image for game (Changes {Alphas + Pixles} for blitting.) 
    # convert_alpha optimizes image for game (Changes Pixles only for blitting.) 

    gameSprites ['numbers'] = (

        pygame.image.load('gallery/sprites/0.png').convert_alpha(),
        pygame.image.load('gallery/sprites/1.png').convert_alpha(),
        pygame.image.load('gallery/sprites/2.png').convert_alpha(),
        pygame.image.load('gallery/sprites/3.png').convert_alpha(),
        pygame.image.load('gallery/sprites/4.png').convert_alpha(),
        pygame.image.load('gallery/sprites/5.png').convert_alpha(),
        pygame.image.load('gallery/sprites/6.png').convert_alpha(),
        pygame.image.load('gallery/sprites/7.png').convert_alpha(),
        pygame.image.load('gallery/sprites/8.png').convert_alpha(),
        pygame.image.load('gallery/sprites/9.png').convert_alpha(),

    ) # --> This is a tuple.

    gameSprites ['message'] = pygame.image.load('gallery/sprites/message.png').convert_alpha()
    gameSprites ['base'] = pygame.image.load('gallery/sprites/base.png').convert_alpha()
    gameSprites ['background'] = pygame.image.load(background).convert()
    gameSprites ['player'] = pygame.image.load(player).convert_alpha()

    gameSprites ['pipe'] = (
        pygame.transform.rotate(pygame.image.load(pipe).convert_alpha(),180),
        pygame.image.load(pipe).convert_alpha()
        )  # --> This is a tuple.


    # Game Sounds:

    gameSounds['die'] = pygame.mixer.Sound('gallery/audio/die.wav')
    gameSounds['hit'] = pygame.mixer.Sound('gallery/audio/hit.wav')
    gameSounds['wing'] = pygame.mixer.Sound('gallery/audio/wing.wav')
    gameSounds['point'] = pygame.mixer.Sound('gallery/audio/point.wav')
    gameSounds['smoosh'] = pygame.mixer.Sound('gallery/audio/swoosh.wav')


    # Infinite loop:

    while True:
        welcomeScreen() # --> Shows Welcome Screen.
        mainGame() # --> Main Game Function Call.