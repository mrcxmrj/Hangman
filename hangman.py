"""Simple Hangman Game"""
# Import and initialize the pygame library
import pygame
import pygame.freetype

pygame.init()

#variables for width and height
x = 500
y = 500

# Set up the drawing window
screen = pygame.display.set_mode([x, y])

# define the RGB value for white 
#  green, blue colour
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

#create a font object
font = pygame.font.Font(None, 100)

#generate the word
word = "hello"
password = ""
for letter in word:
    password += "_"
currPassword = " ".join(password)

#create a text object
text = font.render(currPassword, True, blue)

# create a rectangular object for the
# text surface object
textRect = text.get_rect()

# set the center of the rectangular object
textRect.center = (x // 2, y // 2)

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

    # Fill the background with white
    screen.fill((255, 255, 255))

    #print the password
    screen.blit(text, textRect)

    # Draw a solid blue circle in the center
    #pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
