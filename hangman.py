"""
Simple Hangman Game
english dictionary from https://github.com/dwyl/english-words
"""
# Import and initialize the pygame library
import pygame
import pygame.freetype
from time import sleep
import random

pygame.init()

#variables for width and height
x = 1000
y = 500

# Set up the drawing window
screen = pygame.display.set_mode([x, y])

# define the RGB value for white 
#  green, blue colour
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
red = (255, 0, 0)

#create a font object
font = pygame.font.Font(None, 100)

def newGame():
    #generate the word
    with open("dictionary.txt", "r") as dictionary:
        words = [line for line in dictionary]
    global word 
    word = random.choice(words).strip("\n")
    print(word)
    global password
    password = ""
    for letter in word:
        password += "_"
    global currPassword
    currPassword = " ".join(password)
    global counter
    counter = 0

newGame()
# #generate the word
# with open("dictionary.txt", "r") as dictionary:
#     words = [line for line in dictionary]
# word = random.choice(words).strip("\n")
# print(word)
# password = ""
# for letter in word:
#     password += "_"
# currPassword = " ".join(password)

# counter = 0

#create a text object
text = font.render(currPassword, True, blue)
# create a rectangular object for the
# text surface object
textRect = text.get_rect()
# set the center of the rectangular object
textRect.center = (x // 2, y // 2)

def message(content, color, center=True, xposition=0, yposition=0, fontsize=50):
    messageFont = pygame.font.Font(None, fontsize)
    messageText = messageFont.render(content, True, color)
    messageBox = messageText.get_rect()
    if center:
        messageBox.midtop = ((x//2),(yposition))
    else:
        messageBox.topleft = ((xposition),(yposition))
    screen.blit(messageText, messageBox)


# Run until the user asks to quit
running = True
while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            pressedLetter = pygame.key.name(event.key)
            if pressedLetter in word:
                for index, character in enumerate(word):
                    if character == pressedLetter:
                        password = password[:index] + pressedLetter + password[index+1:]
                currPassword = " ".join(password)
                print(currPassword)
                text = font.render(currPassword, True, blue)
            else:
                counter += 1

    # Fill the background with white
    screen.fill((255, 255, 255))

    if counter == 8:
        message("number of tries:"+str(counter), (0,0,0), False, 0)
        text = font.render(currPassword, True, red)
        #print the password
        screen.blit(text, textRect)
        message("You Lost :(", red)
        pygame.display.flip()

        running = False
        sleep(2)
    elif currPassword == " ".join(word):
        message("number of tries:"+str(counter), (0,0,0), False, 0)
        text = font.render(currPassword, True, green)
        #print the password
        screen.blit(text, textRect)
        message("You Won!", green)
        pygame.display.flip()

        running = False
        sleep(2)
    else:
        message("number of tries:"+str(counter), (0,0,0), False, 0)
        #print the password
        screen.blit(text, textRect)
        pygame.display.flip()

# Done! Time to quit.
pygame.quit()
